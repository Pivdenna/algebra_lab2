import numpy as np

text_message = 'Sorry for the deadline, I did not have light'
print(f"Original message:\n {text_message}")

key_matrix = np.random.randint(0, 256, (len(text_message), len(text_message)))
def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector)
    return encrypted_vector, eigenvalues, eigenvectors

def decrypt_message(encrypted_vector, key_matrix):
    inverse_diagonalized_key_matrix = np.linalg.inv(key_matrix)
    decrypted_vector = np.round(np.dot(inverse_diagonalized_key_matrix, encrypted_vector))
    decrypted_vector = ''.join([chr(num) for num in decrypted_vector])
    print(f'Decrypted message:\n {decrypted_vector}')



encrypted_vector, eigenvalues, eigenvectors = encrypt_message(text_message, key_matrix)
print(f'Encrypted message:\n {encrypted_vector}')
decrypt_message(encrypted_vector, key_matrix)