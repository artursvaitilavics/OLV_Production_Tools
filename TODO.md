



Enabling passes:
  Currently sets passes for all scenes -> layers with name 'img'
  TODOs:
    1. Get layer name from current active layer, and apply passes to all scenes with the same name layer
    2. Create output nodes for every enabled passes


How:
  1: can be done in the same operations module.
    1. function that gets name from active layer and returns the name
    2. variable for name gets this functions value

  2:
    1. Tweak compositor_output_nodes.py so it's not only for creating project
    2. Make a function in it, that is called, when new project is created
    3. Make a dictionary with all possible nodes
    4. Make a function which is called, every time we set some passes in global setttings  -> passes
  

  Important TODO: We must be able to create View_layers globaly for all Scenes