import FWCore.ParameterSet.Config as cms

# $Id: FourVectorHLTOffline_cfi.py,v 1.35 2010/06/01 11:37:12 rekovic Exp $
hltResults = cms.EDAnalyzer("FourVectorHLTOffline",
    dirname = cms.untracked.string("HLT/FourVector/paths"),
    muonRecoCollectionName = cms.untracked.string("muons"),
    plotAll = cms.untracked.bool(False),
    dRMax = cms.untracked.double(4.0),
    ptMax = cms.untracked.double(100.0),
    ptMin = cms.untracked.double(0.0),
		Nbins = cms.untracked.uint32(50),
    referenceBX= cms.untracked.uint32(1),
		NLuminositySegments= cms.untracked.uint32(2000),
		LuminositySegmentSize= cms.untracked.double(23),
		NbinsOneOverEt = cms.untracked.uint32(10000),

		muonEtaMax = cms.untracked.double(2.1),
    muonDRMatch = cms.untracked.double(0.3),

    jetDRMatch = cms.untracked.double(0.3),
    jetL1DRMatch = cms.untracked.double(0.5),
    jetEtMin = cms.untracked.double(5.0),

    electronDRMatch = cms.untracked.double(0.5),
    electronL1DRMatch = cms.untracked.double(0.5),
    electronEtMin = cms.untracked.double(5.0),

    photonDRMatch = cms.untracked.double(0.5),
    photonL1DRMatch = cms.untracked.double(0.5),
    photonEtMin = cms.untracked.double(5.0),

    #tauDRMatch = cms.untracked.double(0.1),

    #bjetDRMatch = cms.untracked.double(0.1),

    #trackDRMatch = cms.untracked.double(0.1),
     SpecialPaths = cms.vstring(
            'HLT_MET45',
            'HLT_L1Tech_HCAL_HF_coincidence_PM',
            'HLT_L1_BscMinBiasOR_BptxPlusORMinus',
            'HLT_MinBiasBSC',
            'HLT_MinBiasBSC_OR',
            'HLT_MinBiasEcal', 
            'HLT_MinBiasHcal', 
            'HLT_MinBiasPixel_SingleTrack', 
            'HLT_ZeroiasPixel_SingleTrack', 
            'HLT_L1_BPTX', 
            'HLT_ZeroBias'
      ),

    paths = cms.VPSet(
             cms.PSet(
              pathname = cms.string("HLT_"),
              denompathname = cms.string("MinBias")  
             ),
             cms.PSet(
              pathname = cms.string("EG"),
              denompathname = cms.string("Mu")  
             ),
             cms.PSet(
              pathname = cms.string("EG"),
              denompathname = cms.string("HLT_Mu3")  
             ),
             cms.PSet(
              pathname = cms.string("Jet"),
              denompathname = cms.string("Mu")  
             ),
             cms.PSet(
              pathname = cms.string("Jet"),
              denompathname = cms.string("HLT_Mu3")  
             ),
             cms.PSet(
              pathname = cms.string("Ele"),
              denompathname = cms.string("Mu")  
             ),
             cms.PSet(
              pathname = cms.string("Ele"),
              denompathname = cms.string("HLT_Mu3")  
             ),
             cms.PSet(
              pathname = cms.string("Pho"),
              denompathname = cms.string("Mu")  
             ),
             cms.PSet(
              pathname = cms.string("Pho"),
              denompathname = cms.string("HLT_Mu3")  
             ),
             cms.PSet(
              pathname = cms.string("Tau"),
              denompathname = cms.string("Mu")  
             ),
             cms.PSet(
              pathname = cms.string("MET"),
              denompathname = cms.string("Mu")  
             ),
             cms.PSet(
              pathname = cms.string("Mu"),
              denompathname = cms.string("Jet")  
             ),
             cms.PSet(
              pathname = cms.string("Mu"),
              denompathname = cms.string("Jet15U")  
             )
    ),
    JetIDParams  = cms.PSet(
        useRecHits      = cms.bool(True),
        hbheRecHitsColl = cms.InputTag("hbhereco"),
        hoRecHitsColl   = cms.InputTag("horeco"),
        hfRecHitsColl   = cms.InputTag("hfreco"),
        ebRecHitsColl   = cms.InputTag("ecalRecHit", "EcalRecHitsEB"),
        eeRecHitsColl   = cms.InputTag("ecalRecHit", "EcalRecHitsEE")
    ),

                          
     # this is I think MC and CRUZET4
    triggerSummaryLabel = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
    triggerResultsLabel = cms.InputTag("TriggerResults","","HLT"),
    processname = cms.string("HLT")

    # this is data (CRUZET I or II best guess)
    #triggerSummaryLabel = cms.InputTag("hltTriggerSummaryAOD","","FU"),
    #triggerResultsLabel = cms.InputTag("TriggerResults","","FU"),
    #processname = cms.string("FU")

 )
