# This is a vectorized implementation of the LCB cipher, compatible with our optimizer and neural distinguisher.
 
#### ADDING A CIPHER
# In order to be compatible with this repo, a cipher implementation must:
# - Provide plain_bits and key_bits variables, giving respectively the number of bits in the plaintext and in the key.
# - Provide a vectorized “encrypt(p, k, r)” function, that takes as input, for n samples:
#       - An n by plain_bits binary matrix p of numpy.uint8 for the plaintexts;
#       - An n by key_bits binary matrix of numpy.uint8 for the keys;
#       - A number of rounds r.
# The encrypt function must return an n by plain_bits matrix of numpy.uint8 containing the ciphertexts. The encrypt function in the provided in this file exemplifies the use of the functions “convert_to_binary” and “convert_from_binary” to translate between binary matrices and the native format of the cipher implementation.
 
import numpy as np
 
plain_bits = 32
key_bits = 64
word_size = 16
 
def WORD_SIZE():
    return(16);
 
S =  [12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2];
P = [12,3,7,13,9,8,14,1,4,15,10,5,16,2,6,11];
L = [1,5,9,13,15,11,7,3,2,6,10,14,16,12,8,4];
k1 = None
k2 = None
k3 = None
k4 = None
 
 
def substitute(x, s):
    #print("X:",x)
    y = np.zeros_like(x)
    for i in range(x.size):
        temp = x[i]
        y[i] += s[(temp % 16)]
        temp = temp >> 4
        y[i] += (s[temp % 16] << 4)
        temp = temp >> 4
        y[i] += (s[temp % 16] << 8)
        temp = temp >> 4
        y[i] += (s[temp % 16] << 12)
    #print("HIIIIIIIIIIIIIIII")
    #print("y", y)
    return y
 
def permute(x,p):
    y = x*0;
    for i in range(0,16):
      y+=(x%2)*(2**(16-p[15-i]));
      x=x>>1;
    #print("permute:", y)
    return y;
 
def enc_one_round(p,k):
    l,r =  p[0], p[1];
    k1, k2 = k[0], k[1];
    #p2 = S(p2)
    r1 = substitute(r, S);
 
    #p2 = P(p2)
    r2 = permute(r1, P);
 
    #p2 = L(p2)
    r3 = permute(r2,L);
 
    #p2 = p2^k
    r4 = r3 ^ k2
 
    #p1 = S(p1)
    l1 = substitute(l, S);
 
    #p1 = P(p1)
    l2 = permute(l1, P);
 
    #p1 = L(p1)
    l3 = permute(l2,L);
 
    #p1 = p1^k
    l4 = l3 ^ k1
 
    return r4, l4;
 
# The encrypt function must adhere to this format, with p and k being binary matrices representing the plaintexts and the key, and the return value being a binary matrix as well.
def encrypt(p, ks, nr):
    p = convert_from_binary(p)
    global k1, k2, k3, k4
    x, y = p[:, 0], p[:, 1];
    #print("BRO!",x,y)
    ks = convert_from_binary(ks).transpose()
    #print(ks)
    #ks = ks.reshape(4,-1);
    k1, k2, k3, k4 = ks[0], ks[1], ks[2], ks[3]
    #print("k1,k2,k3,k4:", k1, k2, k3, k4)
    if(nr == 1):
    	x, y = enc_one_round((x,y), (k1,k2));
    elif(nr%2 == 0): 
        for k in range(int(nr/2)):
                x, y = enc_one_round((x,y), (k1,k2));
                k1 = substitute(k1, S)
                k1 = permute(k1, P)
                k1 = permute(k1, L)
                k2 = substitute(k2, S)
                k2 = permute(k2, P)
                k2 = permute(k2, L)
                x, y = enc_one_round((x,y), (k3,k4));
                k3 = substitute(k3, S)
                k3 = permute(k3, P)
                k3 = permute(k3, L)
                k4 = substitute(k4, S)
                k4 = permute(k4, P)
                k4 = permute(k4, L)
    
    else:
        for k in range(int(nr/2)):
                x, y = enc_one_round((x,y), (k1,k2));
                k1 = substitute(k1, S)
                k1 = permute(k1, P)
                k1 = permute(k1, L)
                k2 = substitute(k2, S)
                k2 = permute(k2, P)
                k2 = permute(k2, L)
                x, y = enc_one_round((x,y), (k3,k4));
                k3 = substitute(k3, S)
                k3 = permute(k3, P)
                k3 = permute(k3, L)
                k4 = substitute(k4, S)
                k4 = permute(k4, P)
                k4 = permute(k4, L)
        x, y = enc_one_round((x,y), (k1,k2));
    	
    #print("X and y:", x, y)
    
    return convert_to_binary([x, y]);
 
#convert_to_binary takes as input an array of ciphertext pairs
#where the first row of the array contains the lefthand side of the ciphertexts,
#the second row contains the righthand side of the ciphertexts,
#the third row contains the lefthand side of the second ciphertexts,
#and so on
#it returns an array of bit vectors containing the same data
def convert_to_binary(arr):
  X = np.zeros((len(arr) * WORD_SIZE(),len(arr[0])),dtype=np.uint8);
  for i in range(len(arr) * WORD_SIZE()):
    index = i // WORD_SIZE();
    offset = WORD_SIZE() - (i % WORD_SIZE()) - 1;
    X[i] = (arr[index] >> offset) & 1;
  X = X.transpose();
  return(X);
 
# Convert_from_binary takes as input an n by num_bits binary matrix of type np.uint8, for n samples, 
# and converts it to an n by num_words array of type dtype.
def convert_from_binary(arr, _dtype=np.uint16):
  num_words = arr.shape[1]//WORD_SIZE()
  X = np.zeros((len(arr), num_words),dtype=_dtype);
  for i in range(num_words):
    for j in range(WORD_SIZE()):
        pos = WORD_SIZE()*i+j
        X[:, i] += 2**(WORD_SIZE()-1-j)*arr[:, pos]
  return(X);
 
 
"""def check_testvectors():
  p = np.uint16([0xCED4, 0xB5C6]).reshape(-1, 1)
  k = np.uint16([0xD63A, 0x529E, 0xCC92,0xD353]).reshape(-1, 1)
  pb = convert_to_binary(p)
  kb = convert_to_binary(k)
  c = convert_from_binary(encrypt(pb, kb, 10))
  assert np.all(c[0] == [0xCDAA, 0x4BBD])
 
check_testvectors()"""
