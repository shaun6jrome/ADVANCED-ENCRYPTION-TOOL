# ADVANCED-ENCRYPTION-TOOL

*COMPANY NAME* : CODTECH IT SOLUTIONS


*NAME* : SHAUN JEROME


*INTERN ID* : CT04DM953


*DOMAIN* : Cyber Security & Ethical Hacking


*DURATION* : 4 WEEKS


*MENTOR* : NEELA SANTHOSH



*DESCRIPTION* 

In the age of rapidly evolving digital communication, the confidentiality and security of personal and sensitive data have become a critical concern. As data continues to move across networks and storage devices, the threat of unauthorized access and data breaches remains a growing challenge. The Advanced Encryption Tool addresses this concern by enabling users to encrypt and decrypt files with a robust and secure algorithm, providing a reliable way to protect digital assets.

Objective of the Project

The primary goal of this tool is to offer a user-friendly, secure, and portable encryption solution using AES-256 (Advanced Encryption Standard), a widely trusted and adopted symmetric encryption technique. By encrypting files with AES-256, the tool ensures that only users with the correct password or key can decrypt and access the original content, thereby maintaining confidentiality and integrity.

This tool is ideal for ethical hackers, penetration testers, security researchers, and general users who wish to safeguard files from unauthorized access, particularly when sharing over networks or storing on cloud services.

Key Features
	•	AES-256 Encryption: Implements AES (Advanced Encryption Standard) with a 256-bit key size, offering strong resistance to brute-force attacks.
	•	Password-Based Encryption: Files are encrypted using a key derived from a user-provided password, ensuring simplicity and usability.
	•	File Agnostic: Works with any type of file—text documents, PDFs, images, executables, etc.
	•	Easy Command-Line Interface (CLI): Users can run the tool with simple command-line instructions to encrypt or decrypt files.
	•	Secure Key Derivation: Utilizes PBKDF2 (Password-Based Key Derivation Function 2) with salting and multiple iterations to strengthen password-derived keys.
	•	Error Handling and Feedback: Provides meaningful terminal output for both successful and unsuccessful operations.
	•	Modular and Readable Code: Clean Python structure with modular functions to support maintainability and scalability.

How It Works
	1.	Encryption:
	•	The user selects a file and enters a password.
	•	A secure encryption key is derived using PBKDF2 with a randomly generated salt.
	•	The file contents are encrypted using AES in CBC (Cipher Block Chaining) mode.
	•	The resulting encrypted data, along with the salt and IV (Initialization Vector), is saved to a new file with a .enc extension.
	2.	Decryption:
	•	The user selects an encrypted file and provides the same password used during encryption.
	•	The tool extracts the salt and IV, regenerates the key, and attempts decryption.
	•	If the password is correct and the file is not corrupted, the original data is restored.

Libraries Used
	•	cryptography – For implementing AES encryption and secure key derivation.
	•	os, sys – For file handling and user interaction.
	•	argparse – For building the command-line interface.

Security Considerations
	•	This tool avoids storing or logging passwords.
	•	Key derivation includes random salting and a high number of iterations.
	•	Encrypted files contain only the ciphertext, salt, and IV—no metadata or identifying information.

Note: Although the tool uses strong cryptographic practices, its real-world security depends on proper usage (e.g., choosing strong passwords, not sharing files publicly, and protecting the encryption key).

Use Cases
	•	Encrypting confidential documents before uploading them to cloud storage.
	•	Securing sensitive research data or reports.
	•	Protecting files during transfers over USB or email.
	•	Practicing cybersecurity and cryptography concepts in academic settings.

Conclusion
The Advanced Encryption Tool is a practical demonstration of applying cryptographic techniques in real-world scenarios. It empowers users to take control of their data security by providing a simple yet powerful way to encrypt and decrypt files using AES-256. This project not only showcases programming and cybersecurity skills but also raises awareness about the importance of data protection in the digital era.


<img width="955" alt="Image" src="https://github.com/user-attachments/assets/716c4ab1-349c-4266-b597-99ac797b7108" />
<img width="929" alt="Image" src="https://github.com/user-attachments/assets/fa720867-2d23-4807-9757-baa95402d7c9" />
