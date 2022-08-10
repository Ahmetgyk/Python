işaret = [".", ",", " ", ":" ,"?"]

class Caesar():
    def __init__(self, shift):
        self.shift = shift;
        pass
    
    def encoder(self, st):
        en = "";
        sf = 0;
        
        st = st.lower();
        for i in st:
            iş = False;
            for n in işaret:
                if(i == n):
                    iş = True;   
                
            if(iş):
                en = en + i; 
            else:
                en = en + chr(ord(i) + self.shift + sf);
                 
            sf += 1;
            
        print(en);
        return en
    
    def decoder(self, st):
        de = "";
        sf = 0;
        
        st = st.lower();
        for i in st:
            iş = False;
            for n in işaret:
                if(i == n):
                    iş = True;   
                
            if(iş):
                de = de + i; 
            else:
                de = de + chr(ord(i) - self.shift - sf);
                 
            sf += 1;
            
        print(de);
        return de
    
sifre = Caesar(8).encoder("Abci:  Cdf,gli?");
Caesar(8).decoder(sifre);