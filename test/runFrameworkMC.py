from JMEAnalysis.JMEValidator.FrameworkConfiguration import createProcess

import FWCore.ParameterSet.Config as cms

process = createProcess(isMC = True, globalTag = "MCRUN2_74_V7")

process.source.fileNames = cms.untracked.vstring(
        '/store/relval/CMSSW_7_4_1/RelValFS_TTbar_13_PUAVE35/MINIAODSIM/PU25ns_MCRUN2_74_V9_FastSim-v1/00000/1868AA47-19ED-E411-9D57-0025905A6080.root'
    )

