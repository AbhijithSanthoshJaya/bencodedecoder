def is_ascii(string:str):
    return all(ord(char) < 127 and ord(char) > 31 for char in string )
    
def is_decimal(string:str):
    return all(ord(char) < 57 and ord(char) > 48 for char in string )

def decodeBenInt(bencodedData:str):
    try:
        lastChar = bencodedData.index('e')
        strInteger = bencodedData[1:lastChar]
        if(is_decimal(strInteger)):
            decodedData = int(strInteger)
            bencodedData = bencodedData[lastChar:]
            return decodedData, bencodedData
    except Exception as e:
        print(e)
        return None,None

def decodeBenString(bencodedData:str):
    try:
        stringBegin = bencodedData.index(':')
        dataLength = int(bencodedData[0:stringBegin])
        if(is_ascii(bencodedData)):
            #print(stringBegin)
            decodedData = bencodedData[stringBegin+1 : stringBegin + dataLength+1]
            bencodedData = bencodedData[stringBegin + dataLength + 1:]
            return decodedData, bencodedData
        else:
            raise Exception('The string contains non-ascii charachters, violating the bencoding standard for byte strings')
    except Exception as e:
        print(e) 
        return None,None
        
def decodeBenList(bencodedData:str):
    try:
        decodedList = []
        bencodedData = bencodedData[1:]
        while(bencodedData[0] != 'e'):  
            decodedData, bencodedData = decoderMapper(bencodedData)
            print(bencodedData)
            decodedList.append(decodedData)
        return decodedList, bencodedData[1:]
    except Exception as e:
        print(e) 
        return None,None

def decoderMapper(bencodedData:str):
    try:
        length = len(bencodedData)
        bencodedType = None
        if(bencodedData[0] in ['l', 'i', 'd'] and bencodedData[length-1] == 'e'):
            bencodedType = bencodedData[0]
        elif( ':' in bencodedData):
            bencodedType = 's'
        bencode_mapper = {
            "i": decodeBenInt,
            "s": decodeBenString
        }
        if(bencodedType in bencode_mapper.keys()):
            decodedData, bencodedData = bencode_mapper[bencodedType](bencodedData)
            return decodedData, bencodedData
        else:
            raise Exception('Invalid bencoded input')
    except Exception as e:
        print(e)
        return None,None

def decoder(bencodedData):
    decodedData,bencodedData = decoderMapper(bencodedData)
    return decodedData

   
