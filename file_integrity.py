
import hashlib, hmac
def calculate_file_hash(file_path, algorithm='sha256'):
    """
    Υπολογίζει την τιμή hash ενός αρχείου χρησιμοποιώντας τον
    καθορισμένο αλγόριθμο.
    ΠΡΟΣΟΧΗ: Αυτή η συνάρτηση έχει εσκεμμένα κάποια κενά που
    πρέπει να συμπληρώσετε.
    
    Args:
    file_path (str): Διαδρομή προς το αρχείο
    algorithm (str): Ο αλγόριθμος hash (προεπιλογή: 'sha256')
    
    Returns:
    str: Η hex τιμή του hash ή None αν αποτύχει
    """

    try:
        hash_obj = hashlib.new(algorithm)
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(65536), b''):
                hash_obj.update(chunk)
        return hash_obj.hexdigest() or None
    
    except:
        return None
    
def secure_hash_compare(hash1,hash2):
    return hmac.compare_digest(hash1.lower(), hash2.lower())

def verify_file_integrity(original_hash, current_hash):
    """
    Ελέγχει αν μια αρχική hash τιμή ταιριάζει με την τρέχουσα.
    
    Args:
    original_hash (str): Η αρχική hash τιμή
    current_hash (str): Η τρέχουσα hash τιμή

    Returns:
    bool: True αν ταιριάζουν, False διαφορετικά
    """
    if not original_hash or not current_hash: return False
    if len(original_hash) != len(current_hash): return False

    return secure_hash_compare(original_hash, current_hash)

def main():
    print("Εργαστηριακή Άσκηση - Έλεγχος Ακεραιότητας Αρχείων")
    while True:
        print("\nMenu:")
        print("1. Calculate Hash file")
        print("2. Verify Hash file")
        print("3. Exit")
        try:
            choice = int(input("Choose option (1-3): "))
        except ValueError:
            choice = -1
        match choice:
            case 1:
                handle_hash_calculation()
            case 2:
                handle_integrity_check()
            case 3:
                print("Exiting program")
                break
            case _:
                print("Invalid option, choose 1, 2 or 3.")

def handle_hash_calculation():
    algorithims = {
        '1': 'md5',
        '2': 'sha1',
        '3': 'sha256',
        '4': 'sha3_256'
    }

    print("\nChoose hash algorithim:")
    print("1. MD5")
    print("2. SHA-1")
    print("3. Sha-256")
    print("4. Sha3-256")

    alg_choice = input("Choose (1-4): ").lower()

    algorithim = algorithims.get(alg_choice, 'sha256')

    file_path = input("Give file path: ")
    file_hash = calculate_file_hash(file_path, algorithim)
    if file_hash:
        print(f"Hash ({algorithim.upper()}) of file is {file_hash}")

def handle_integrity_check():
    file_path = input("Give file path: ")
    algorithim = input("Give hash algorithim (ex: sha256): ").lower()
    original_hash = input("Give Original hash value: ").strip()

    current_hash = calculate_file_hash(file_path, algorithim)
    if current_hash:
        if verify_file_integrity(original_hash, current_hash):
            print("File is intact")
        else:
            print("File has been compromised")
    
if __name__ == "__main__":
    main()