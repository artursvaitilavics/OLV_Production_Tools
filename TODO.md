1. Remove img socket, and default denoise, when starting to use passes,   
2. refactor create render layer node, as its comming in repeaditly
    - check if there is layer node for each view layer
    - if no, create
3. Denoise node to check if layer is correct, not only pass. currently connecting to all Denoise socekts inf File Output node.

6. Weird passes, like CryptoMattes, render times and indexes, to be removed from list temporeraly



----------------
Commit
------------------


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

