#!/usr/bin/env pythonfrom main_window import MainWindowfrom PyQt4 import QtGuiimport sys, osdef main():    app = QtGui.QApplication(sys.argv)    window=MainWindow()    window.show()    sys.exit(app.exec_())if __name__ == "__main__":    main()#category is determined by the object your plugins it inherit from#Default means that everything from yapsy.IPlugin.IPlugin is accepted#can be changed by adding parameter to the declaration of the pluginmanager#http://yapsy.sourceforge.net/yapsy.PluginManager.PluginManager-class.html#__init__#the list contains Plugininfo objects#http://yapsy.sourceforge.net/yapsy.PluginManager.PluginInfo-class.html#list = var.getPluginsOfCategory("Default")#print list#for item in list:#    print "item:"#    print item    #the pluginobject itself can be retrieved from PluginInfo    #with .plugin_object#    pluginobject = item.plugin_object    #now you can call the methods from your plugin#    pluginobject.test()#get the plugin by name this returns the plugin (not the info)#for the PluginInfo object --&gt;#plugin = var.activatePluginByName("yournamehere")#again methods can be called#plugin.test()#plugin code