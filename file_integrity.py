
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
    # TODO: Συμπληρώστε τον κώδικα για ανάγνωση του αρχείου
    #και υπολογισμό hash
    # Υπόδειξη: Χρησιμοποιήστε μπλοκ ανάγνωσης για
    #αποδοτικότητα με μεγάλα αρχεία
    
    try:
        hash_obj = hashlib.new(algorithm)
    
    except:
        pass
    
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
    TODO: Συμπληρώστε τη λογική επαλήθευσης
    TODO: Προσθέστε έλεγχο για κενές ή μη έγκυρες τιμές hash
    """
    pass

def main():
    print("Εργαστηριακή Άσκηση - Έλεγχος Ακεραιότητας Αρχείων")
    # TODO: Δημιουργήστε ένα μενού επιλογών για τους διαφορετικούς αλγορίθμους hash
    # (MD5, SHA-1, SHA-256, SHA3-256)
    file_path = input("Εισάγετε τη διαδρομή του αρχείου: ")
    # TODO: Προσθέστε λειτουργικότητα για:
    # 1. Υπολογισμό και εμφάνιση hash τιμής
    # 2. Επαλήθευση ακεραιότητας έναντι γνωστής hash τιμής
    # TODO: Προσθέστε επεξεργασία σφαλμάτων για μη υπάρχοντα αρχεία

if __name__ == "__main__":
    main()