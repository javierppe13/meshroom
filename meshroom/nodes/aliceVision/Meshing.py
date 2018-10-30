__version__ = "2.0"

from meshroom.core import desc


class Meshing(desc.CommandLineNode):
    commandLine = 'aliceVision_meshing {allParams}'

    cpu = desc.Level.INTENSIVE
    ram = desc.Level.INTENSIVE

    inputs = [
        desc.File(
            name='input',
            label='Input',
            description='SfMData file.',
            value='',
            uid=[0],
        ),
        desc.File(
            name='imagesFolder',
            label='Images Folder',
            description='Use images from a specific folder. Filename should be the image uid.',
            value='',
            uid=[0],
        ),
        desc.File(
            name="depthMapFolder",
            label='Depth Maps Folder',
            description='Input depth maps folder',
            value='',
            uid=[0],
        ),
        desc.File(
            name="depthMapFilterFolder",
            label='Filtered Depth Maps Folder',
            description='Input filtered depth maps folder',
            value='',
            uid=[0],
        ),
        desc.BoolParam(
            name='estimateSpaceFromSfM',
            label='Estimate Space From SfM',
            description='Estimate the 3d space from the SfM',
            value=True,
            uid=[0],
        ),
        desc.IntParam(
            name='minObservations',
            label='Min Observations For SfM Space Estimation',
            description='Minimum number of observations for SfM space estimation.',
            value=3,
            range=(0, 100, 1),
            uid=[0],
        ),
        desc.IntParam(
            name='maxInputPoints',
            label='Max Input Points',
            description='Max input points loaded from depth map images.',
            value=50000000,
            range=(500000, 500000000, 1000),
            uid=[0],
        ),
        desc.IntParam(
            name='maxPoints',
            label='Max Points',
            description='Max points at the end of the depth maps fusion.',
            value=5000000,
            range=(100000, 10000000, 1000),
            uid=[0],
        ),
        desc.IntParam(
            name='maxPointsPerVoxel',
            label='Max Points Per Voxel',
            description='Max points per voxel',
            value=1000000,
            range=(500000, 30000000, 1000),
            uid=[0],
        ),
        desc.IntParam(
            name='minStep',
            label='Min Step',
            description='The step used to load depth values from depth maps is computed from maxInputPts. '
            'Here we define the minimal value for this step, so on small datasets we will not spend '
            'too much time at the beginning loading all depth values.',
            value=2,
            range=(1, 20, 1),
            uid=[0],
        ),
        desc.ChoiceParam(
            name='partitioning',
            label='Partitioning',
            description='',
            value='singleBlock',
            values=('singleBlock', 'auto'),
            exclusive=True,
            uid=[0],
        ),
        desc.ChoiceParam(
            name='repartition',
            label='Repartition',
            description='',
            value='multiResolution',
            values=('multiResolution', 'regularGrid'),
            exclusive=True,
            uid=[0],
        ),
        desc.FloatParam(
            name='angleFactor',
            label='angleFactor',
            description='angleFactor',
            value=15.0,
            range=(0.0, 200.0, 1.0),
            uid=[0],
        ),
        desc.FloatParam(
            name='simFactor',
            label='simFactor',
            description='simFactor',
            value=15.0,
            range=(0.0, 200.0, 1.0),
            uid=[0],
        ),
        desc.FloatParam(
            name='pixSizeMarginInitCoef',
            label='pixSizeMarginInitCoef',
            description='pixSizeMarginInitCoef',
            value=2.0,
            range=(0.0, 10.0, 0.1),
            uid=[0],
        ),
        desc.FloatParam(
            name='pixSizeMarginFinalCoef',
            label='pixSizeMarginFinalCoef',
            description='pixSizeMarginFinalCoef',
            value=4.0,
            range=(0.0, 10.0, 0.1),
            uid=[0],
        ),
        desc.FloatParam(
            name='voteMarginFactor',
            label='voteMarginFactor',
            description='voteMarginFactor',
            value=4.0,
            range=(0.1, 10.0, 0.1),
            uid=[0],
        ),
        desc.FloatParam(
            name='contributeMarginFactor',
            label='contributeMarginFactor',
            description='contributeMarginFactor',
            value=2.0,
            range=(0.0, 10.0, 0.1),
            uid=[0],
        ),
        desc.FloatParam(
            name='simGaussianSizeInit',
            label='simGaussianSizeInit',
            description='simGaussianSizeInit',
            value=10.0,
            range=(0.0, 50.0, 0.1),
            uid=[0],
        ),
        desc.FloatParam(
            name='simGaussianSize',
            label='simGaussianSize',
            description='simGaussianSize',
            value=10.0,
            range=(0.0, 50.0, 0.1),
            uid=[0],
        ),
        desc.FloatParam(
            name='minAngleThreshold',
            label='minAngleThreshold',
            description='minAngleThreshold',
            value=1.0,
            range=(0.0, 10.0, 0.01),
            uid=[0],
        ),
        desc.BoolParam(
            name='refineFuse',
            label='Refine Fuse',
            description='Refine depth map fusion with the new pixels size defined by angle and similarity scores.',
            value=True,
            uid=[0],
        ),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='''verbosity level (fatal, error, warning, info, debug, trace).''',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            uid=[],
        ),
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output mesh",
            description="Output mesh (OBJ file format).",
            value="{cache}/{nodeType}/{uid0}/mesh.obj",
            uid=[],
            ),
        desc.File(
            name="outputDenseReconstruction",
            label="Output reconstruction",
            description="Output dense reconstruction (BIN file format).",
            value="{cache}/{nodeType}/{uid0}/denseReconstruction.bin",
            uid=[],
            group="",
            ),
    ]
