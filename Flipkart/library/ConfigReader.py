import configparser

def readConfigData(section,key):
    config = configparser.ConfigParser()
    config.read("./configurationFiles/Config.cfg")
    return config.get(section,key)


def fetchElement(section,key):
    config = configparser.ConfigParser()
    config.read("./configurationFiles/Elements.cfg")
    return config.get(section,key)