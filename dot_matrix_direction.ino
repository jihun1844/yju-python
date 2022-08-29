int anode[8] = {9,A2,A3,6,2,7,11,12};
int cathode[8] = {5,10,4,8,A0,3,A1,A4};
int num=0;

int matrixX[8][8] = {
  {1,0,0,0,0,0,0,1},
  {0,1,0,0,0,0,1,0},
  {0,0,1,0,0,1,0,0},
  {0,0,0,1,1,0,0,0},
  {0,0,0,1,1,0,0,0},
  {0,0,1,0,0,1,0,0},
  {0,1,0,0,0,0,1,0},
  {1,0,0,0,0,0,0,1}
};

int matrixHOL[8][8] = { 
  {0,0,1,0,0,1,0,0},
  {0,1,0,1,1,0,1,0},
  {1,0,1,0,0,1,0,1},
  {0,1,0,1,1,0,1,0},
  {0,1,0,1,1,0,1,0},
  {1,0,1,0,0,1,0,1},
  {0,1,0,1,1,0,1,0},
  {0,0,1,0,0,1,0,0}
};

int matrixUP[8][8] = { 
  {0,0,0,1,1,0,0,0},
  {0,0,1,1,1,1,0,0},
  {0,1,1,1,1,1,1,0},
  {1,1,1,1,1,1,1,1},
  {0,0,0,1,1,0,0,0},
  {0,0,0,1,1,0,0,0},
  {0,0,0,1,1,0,0,0},
  {0,0,0,1,1,0,0,0}
};

int matrixDOWN[8][8] = { 
  {0,0,0,1,1,0,0,0},
  {0,0,0,1,1,0,0,0},
  {0,0,0,1,1,0,0,0},
  {0,0,0,1,1,0,0,0},
  {1,1,1,1,1,1,1,1},
  {0,1,1,1,1,1,1,0},
  {0,0,1,1,1,1,0,0},
  {0,0,0,1,1,0,0,0}
};

int matrixLEFT[8][8] = { 
  {0,0,0,1,0,0,0,0},
  {0,0,1,1,0,0,0,0},
  {0,1,1,1,0,0,0,0},
  {1,1,1,1,1,1,1,1},
  {1,1,1,1,1,1,1,1},
  {0,1,1,1,0,0,0,0},
  {0,0,1,1,0,0,0,0},
  {0,0,0,1,0,0,0,0}
};


int matrixRIGHT[8][8] = { 
  {0,0,0,0,1,0,0,0},
  {0,0,0,0,1,1,0,0},
  {0,0,0,0,1,1,1,0},
  {1,1,1,1,1,1,1,1},
  {1,1,1,1,1,1,1,1},
  {0,0,0,0,1,1,1,0},
  {0,0,0,0,1,1,0,0},
  {0,0,0,0,1,0,0,0}
};

int matrixUPLEFT[8][8] = { 
  {1,1,1,1,1,1,1,0},
  {1,1,1,1,1,1,0,0},
  {1,1,1,1,1,0,0,0},
  {1,1,1,1,1,0,0,0},
  {1,1,1,1,1,1,0,0},
  {1,1,0,0,1,1,1,0},
  {1,0,0,0,0,1,1,1},
  {0,0,0,0,0,0,1,0}
};

int matrixUPRIGHT[8][8] = { 
  {0,1,1,1,1,1,1,1},
  {0,0,1,1,1,1,1,1},
  {0,0,0,1,1,1,1,1},
  {0,0,0,1,1,1,1,1},
  {0,0,1,1,1,1,1,1},
  {0,1,1,1,0,0,1,1},
  {1,1,1,0,0,0,0,1},
  {0,1,0,0,0,0,0,0}
};

int matrixDOWNRIGHT[8][8] = { 
  {0,1,0,0,0,0,0,0},
  {1,1,1,0,0,0,0,1},
  {0,1,1,1,0,0,1,1},
  {0,0,1,1,1,1,1,1},
  {0,0,0,1,1,1,1,1},
  {0,0,0,1,1,1,1,1},
  {0,0,1,1,1,1,1,1},
  {0,1,1,1,1,1,1,1}
};

int matrixDOWNLEFT[8][8] = { 
  {0,0,0,0,0,0,1,0},
  {1,0,0,0,0,1,1,1},
  {1,1,0,0,1,1,1,0},
  {1,1,1,1,1,1,0,0},
  {1,1,1,1,1,0,0,0},
  {1,1,1,1,1,0,0,0},
  {1,1,1,1,1,1,0,0},
  {1,1,1,1,1,1,1,0}
};
  



void setup(){
  Serial.begin(9600);
  for(int i=0; i<8;i++){
    pinMode(anode[i],OUTPUT);
    digitalWrite(anode[i],LOW);
    
    pinMode(cathode[i],OUTPUT);
    digitalWrite(cathode[i],HIGH);
  }
  }
void loop(){
  for(int i=0; i<8;i++){
    digitalWrite(anode[i],HIGH);
    digitalWrite(cathode[i],LOW);
  }
  if(Serial.available()>0){
    num = Serial.read();
  }
  Serial.println(num);
  if(num=='8'){
    for( int i=0; i<8;i++){
      for( int j=0; j<8; j++){
        digitalWrite(cathode[j],matrixUP[i][j]);
      }
      digitalWrite(anode[i],LOW);
      delayMicroseconds(1000);
      digitalWrite(anode[i],HIGH);
    }      
  }else if(num=='2'){
    for( int i=0; i<8;i++){
      for( int j=0; j<8; j++){
        digitalWrite(cathode[j],matrixDOWN[i][j]);
      }
      digitalWrite(anode[i],LOW);
      delayMicroseconds(1000);
      digitalWrite(anode[i],HIGH);   
    }
  }else if(num=='6'){
    for( int i=0; i<8;i++){
      for( int j=0; j<8; j++){
        digitalWrite(cathode[j],matrixLEFT[i][j]);
      }
      digitalWrite(anode[i],LOW);
      delayMicroseconds(1000);
      digitalWrite(anode[i],HIGH);         
    }  
  }else if(num=='4'){
    for( int i=0; i<8;i++){
      for( int j=0; j<8; j++){
        digitalWrite(cathode[j],matrixRIGHT[i][j]);
      }
      digitalWrite(anode[i],LOW);
      delayMicroseconds(1000);
      digitalWrite(anode[i],HIGH);    
    }
  }
  else if(num=='9'){
    for( int i=0; i<8;i++){
      for( int j=0; j<8; j++){
        digitalWrite(cathode[j],matrixUPLEFT[i][j]);
      }
      digitalWrite(anode[i],LOW);
      delayMicroseconds(1000);
      digitalWrite(anode[i],HIGH);    
    }
  }
  else if(num=='7'){
    for( int i=0; i<8;i++){
      for( int j=0; j<8; j++){
        digitalWrite(cathode[j],matrixUPRIGHT[i][j]);
      }
      digitalWrite(anode[i],LOW);
      delayMicroseconds(1000);
      digitalWrite(anode[i],HIGH);    
    }
  }
  else if(num=='3'){
    for( int i=0; i<8;i++){
      for( int j=0; j<8; j++){
        digitalWrite(cathode[j],matrixDOWNLEFT[i][j]);
      }
      digitalWrite(anode[i],LOW);
      delayMicroseconds(1000);
      digitalWrite(anode[i],HIGH);    
    }
  }
  else if(num=='1'){
    for( int i=0; i<8;i++){
      for( int j=0; j<8; j++){
        digitalWrite(cathode[j],matrixDOWNRIGHT[i][j]);
      }
      digitalWrite(anode[i],LOW);
      delayMicroseconds(1000);
      digitalWrite(anode[i],HIGH);    
    }
  }
  else if(num=='5'){
    for( int i=0; i<8;i++){
      
      for( int j=0; j<8; j++){
        digitalWrite(cathode[j],matrixHOL[i][j]);
      }
      digitalWrite(anode[i],LOW);
      delayMicroseconds(1000);
      digitalWrite(anode[i],HIGH); 
      
      
    }
  }
   else
   {
    for( int i=0; i<8;i++){
      for( int j=0; j<8; j++){
        digitalWrite(cathode[j],matrixX[i][j]);
      }
      digitalWrite(anode[i],LOW);
      delayMicroseconds(1000);
      digitalWrite(anode[i],HIGH);    
    }
  }
}

 
  
 
