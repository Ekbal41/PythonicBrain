import imp
def check_modules_installed(modules:list):
    """Checks if the given modules are installed
    Returns list of not installed module.
    """
    not_installed_modules = []
    for module_name in modules:
        try:
            imp.find_module(module_name)
        except ImportError as e:
           
            try:
                __import__(module_name)
            except ImportError as e:
                not_installed_modules.append(module_name)

    return not_installed_modules