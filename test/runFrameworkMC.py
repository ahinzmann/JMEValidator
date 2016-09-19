from JMEAnalysis.JMEValidator.FrameworkConfiguration import createProcess

import FWCore.ParameterSet.Config as cms

process = createProcess(isMC = True, globalTag = "80X_mcRun2_asymptotic_2016_miniAODv2")

process.source.fileNames = cms.untracked.vstring(
        '/store/mc/RunIISpring16MiniAODv2/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/0492D89B-7335-E611-AEC3-0090FAA58924.root'
    )

