# Improving_the_security_of_LCB_block_cipher_against_Deep-Learning_based_attacks
The code is with association to the paper "Improving_the_security_of_LCB_block_cipher_against_Deep Learning_based_attacks"

**Under the LCB branch/tag:**

The file "Original_LCB.ipynb" contains the implementation of LCB and also contains the neural distinguisher proposed. The file can be opened using Jupyter notebook or Google Collaborator. The .h5 file and .json files can be exported into the code for testing data.

To generate new .h5 file and .json files, training of the model needs to be done. The code is present in "Original_LCB.ipynb".


**Under the Modified-LCB branch/tag:**

The code is with association to the paper "Improving_the_security_of_LCB_block_cipher_against_Deep Learning_based_attacks"

The file "Modified_LCB.ipynb" contains the implementation of LCB and also contains the neural distinguisher proposed. The file can be opened using Jupyter notebook or Google Collaborator. The .h5 file and .json files can be exported into the code for testing data.

To generate new .h5 file and .json files, training of the model needs to be done. The code is present in "Modified_LCB.ipynb".


**Under the Secure LCB branch/tag:**

The file "Secure_LCB_1c10l_20_depth_3 - 0,F009.ipynb" contains the implementation of LCB and also contains the neural distinguisher proposed. 
The file can be opened using Jupyter notebook or Google Collaborator. 

To generate new .h5 file and .json files, training of the model needs to be done. The code is present in "Secure_LCB_1c10l_20_depth_3 - 0,F009.ipynb".

**Under the NIST-Tests-Data-Generatorbranch/tag:**

The code is with association to the paper "Improving_the_security_of_LCB_block_cipher_against_Deep Learning_based_attacks"

For NISTS tests on Secure LCB: Use "SECURE_LCB_FILE_GENERATION.ipynb" to generate the bitstreams of 10^6. The no. of sequences can be specified in the loop that calls the function make_train_data.

NIST tests can be found in this link: https://csrc.nist.gov/Projects/Random-Bit-Generation/Documentation-and-Software

**Under the Good-input-difference branch/tag:**

The code is with association to the paper "Improving_the_security_of_LCB_block_cipher_against_Deep Learning_based_attacks"
For finding the good input difference: The file "SecureLCB.py" should be kept in the folder of ciphers.

More details about the code can be found in the github link. https://github.com/Crypto-TII/AutoND

To run the neural distinguisher, just check the above link for syntax.
