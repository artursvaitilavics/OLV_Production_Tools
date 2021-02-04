1. Get SymLink paths from json
2. 


1. create a class, that creates nodes,
  - get name from scene and layer - DONE
  - get pass name from properties - DONE
  - create layer node - DONE
  - chose layer by name of active view layer - DONE

  - create input slot in file output node. DONE
  - name slot : project_layer_pass_ DONE
  - connect layer node outputs to correct file output nodes slots


2. Denoising data, 
  - seperate method of creating slots in Output Node
  - seperate method to create new link for denoising data










  Render Layer node's output slots:


Image
Alpha
Depth
Mist
Normal
Vector
UV
Shadow
AO
DiffDir
DiffInd
DiffCol
GlossDir
GlossInd
GlossCol

TransDir
TransInd
TransCol

Emit
Env
VolumeDir
VolumeInd

CryptoObject00
CryptoObject01
CryptoObject02
CryptoMaterial00
CryptoMaterial01
CryptoMaterial02
CryptoAsset00
CryptoAsset01
CryptoAsset02

Noisy Image
Denoising Normal
Denoising Albedo

Denoising Depth
Denoising Shadowing
Denoising Variance
Denoising Intensity
Denoising Clean
Denoise
Image

