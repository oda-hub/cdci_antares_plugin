ANTARES ODA plugin
==========================================
*ANTARES plugin for cdci_data_analysis*


What's the license?
-------------------

ANTARES plugin is distributed under the terms of The MIT License.

Who's responsible?
-------------------
Denys Savchenko, Andrea Tramacere

Astronomy Department of the University of Geneva, Chemin d'Ecogia 16, CH-1290 Versoix, Switzerland

Configuration for deployment
----------------------------
- copy the `conf_file` from `dispatcher_plugin_antares/config_dir/data_server_conf.yml' and place in given directory
- set the environment variable `CDCI_ANTARES_PLUGIN_CONF_FILE` to the path of the file conf_file 
- edit the in `conf_file` the key:
    - `data_server_url:`  
    
