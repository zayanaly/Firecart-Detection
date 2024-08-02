import threading
import time
import yaml
import importlib

plugins = []
values = []

def read_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main():
    config_file = 'config.yaml'
    config = read_config(config_file)

    print("Loading Plugins:")
    for key, value in config.items():
        plugin = importlib.import_module(key)
        plugins.append(getattr(plugin, key)(value))
        values.append(0)
        print(f"\tLoaded {key}")

    print()

    print("Starting Plugins:")
    for plugin in plugins:
        plugin.start()
        print(f"\tStarted {plugin.__module__}")

    print()

    try:
        while 1:
            threads = []
            for index, plugin in enumerate(plugins):
                thread = threading.Thread(target=plugin.compute, args=(values, index))
                threads.append(thread)
                thread.start()

            # Wait for all threads to complete
            for thread in threads:
                thread.join()

            sum = 0
            for index, plugin in enumerate(plugins):
                sum += plugin.weight * values[index]
                values[index] = 0
            
            if sum > 0.5:
                print('Fire!!!🔥\tScore: %0.2f\n' % sum)
            else:
                print('All Good😎\tScore: %0.2f\n' % sum)

            time.sleep(3)

    except Exception as e:
        print(e)
    
    print("Shuttting Down FDS:")
    for plugin in plugins:
        plugin.shutdown()
        print(f"\tShutdown for {plugin.__module__} complete")

if __name__ == "__main__":
    main()
