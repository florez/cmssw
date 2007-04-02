#ifndef DCCFEBLOCK_HH
#define DCCFEBLOCK_HH

#include <iostream>
#include <memory>
#include <stdint.h>
#include <string>
#include <vector>
#include <map>
#include <utility>

#include <DataFormats/EcalDigi/interface/EcalDigiCollections.h>
#include <DataFormats/EcalRawData/interface/EcalRawDataCollections.h>
#include <DataFormats/EcalDetId/interface/EcalDetIdCollections.h>
#include <FWCore/MessageLogger/interface/MessageLogger.h>

#include "DCCDataBlockPrototype.h"

using namespace std;
using namespace edm;

class DCCEventBlock;
class DCCDataUnpacker;

class DCCFEBlock : public DCCDataBlockPrototype {
	
  public :

    DCCFEBlock(DCCDataUnpacker * u,EcalElectronicsMapper * m, DCCEventBlock * e, bool unpack);
    
    virtual ~DCCFEBlock(){ delete [] xtalGains_;}

    void zsFlag(bool zs){ zs_ = zs;}
	 
    virtual void updateCollectors();
    
    void display(ostream & o); 
    
    void unpack(uint64_t ** data, uint * dwToEnd, bool zs, uint expectedTowerID);

    uint getLength(){return blockLength_; }
	 
    			
  protected :
	 
    virtual void unpackXtalData(uint stripID, uint xtalID){};
    
    
    bool zs_;
    uint expTowerID_;
    uint expXtalTSamples_;
    uint unfilteredDataBlockLength_;
    uint lastStripId_;
    uint lastXtalId_;
 
    uint towerId_;	
    uint numbDWInXtalBlock_;
    uint xtalBlockSize_;
    uint nTSamples_; 
    
    uint blockSize_;
    uint bx_;
    uint l1_;
    
    short * xtalGains_;	 
    auto_ptr<EcalTrigTowerDetIdCollection> * invalidTTIds_;
    auto_ptr<EcalTrigTowerDetIdCollection> * invalidBlockLengths_;
	 
   
		
};


#endif
