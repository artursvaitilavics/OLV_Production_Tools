



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
    1. Tweak compositor_output_nodes.py so it's not only for creating project - later
    2. Make a function in it, that is called, when new project is created - later
    3. Make a dictionary with all possible output slots
    4. dictionary gets it value from class properties, if true, then  ouptu slot i created
  

  Important TODO: We must be able to create View_layers globaly for all Scenes