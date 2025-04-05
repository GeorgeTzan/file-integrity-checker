# File Integrity Checker 🔒

![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Build Status](https://github.com/GeorgeTzan/file-integrity-checker/actions/workflows/python-app.yml/badge.svg)

**Πανεπιστήμιο Ιωαννίνων**  
**Τμήμα Πληροφορικής & Τηλεπικοινωνιών**  
**Μάθημα: Ασφάλεια Συστημάτων**  
**Ονοματεπώνυμο: Γεώργιος Τζανόπουλος**  
**ΑΜ: 2846**  

---

## 📑 Table of Contents
1. [Introduction](#-Εισαγωγή)
2. [Installation](#-Εγκατάσταση)
3. [Usage](#Μενού-Επιλογών)
4. [Answers to Questions](#Απαντήσεις-ερωτήσεων-Μέρος-4)
5. [License](#-License)

---

## 📌 Εισαγωγή

Εργαλείο Python για **έλεγχο ακεραιότητας αρχείων** μέσω κρυπτογραφικών hash συναρτήσεων (MD5, SHA-1, SHA-256, SHA3-256).  
**Στόχοι**:  
- Ανίχνευση τυχαίων ή κακόβουλων τροποποιήσεων σε αρχεία  
- Επαλήθευση αυθεντικότητας ληφθέντων αρχείων  
- Εκπαιδευτική εφαρμογή αρχών ασφάλειας δεδομένων  

---

## 📥 Εγκατάσταση

1. Λήψη του κώδικα:
    ```bash
   git clone https://github.com/GeorgeTzan/file-integrity-checker.git
   cd file-integrity-checker
    ```
2. Δημιουργία εικονικού περιβάλλοντος (προτείνεται)
    ```bash
    # UV
    pip install uv
    # Δημιουργία εικονικού περιβάλλοντος
    uv venv
    # Εγκατάσταση εξαρτήσεων από pyproject.toml
    uv sync

    # Ενεργοποίηση περιβάλλοντος (Linux/macOS) -- Optional
    source .venv/bin/activate

    # ή (Windows)
    .\.venv\Scripts\activate
    ```

3. Εκτέλεση αρχείων
    ```bash
    uv run file_integrity.py

    # Εκτέλεση unittests
    uv run file_integrity_unittests.py
    ```

## Μενού Επιλογών

1. Υπολογισμός Hash: Δημιουργία hash τιμής για οποιοδήποτε αρχείο.
2. Επαλήθευση Ακεραιότητας: Σύγκριση αρχείου με γνωστή hash τιμή.
3. Έξοδος

Παράδειγμα Εκτέλεσης:
```bash
1. Calculate Hash file
2. Verify Hash file
3. Exit

Choose option (1-3): 1
Choose hash algorithim (MD5, SHA-1, SHA-256, SHA3-256): SHA-256
File Path: /path/to/file.txt

Hash (SHA-256): a591a6d40bf420...  # Παράδειγμα output
```

## Απαντήσεις ερωτήσεων (Μέρος 4)

# 1. Ασφάλεια

Ερώτημα: Πώς αποφεύγονται επιθέσεις σύγκρισης χρόνου (timing attacks);

Απάντηση:
Χρησιμοποιήθηκε η συνάρτηση hmac.compare_digest() αντί της απλής σύγκρισης (==), καθώς:

* Εκτελείται σε σταθερό χρόνο (constant-time), ανεξάρτητα από το μέγεθος ή την ομοιότητα των hash τιμών.

* Είναι ειδικά σχεδιασμένη για ευαίσθητες συγκρίσεις(πχ passwords, hashes).  

# 2. Αποδοτικότητα
Ερώτημα: Βελτιστοποίηση για μεγάλα αρχεία (>1GB);

Απάντηση:

* Μέθοδος: Ανάγνωση αρχείου ***ανα chunks των 64KB***
* 64KB Βέλτιστο μέγεθος:
    * Προσφέρει ισορροπια μεταξύ:
        * Ελαχιστών syscalls 
        * Χρήση μνήμης (δεν φόρτώνει όλο το αρχείο)

### Υλοποίηση:
```bash
with open(file_path, 'rb') as f:
    for chunk in iter(lambda: f.read(65536), b''):
        hash_obj.update(chunk)
```

# 3. Επέκταση
Ερώτημα: Υποστήριξη πολλαπλών αρχείων;

Απάντηση:
* Δομές Δεδομένων:
    * Dictionaries {file_path: hash} για απλές περιπτώσεις
    * Χρήση Dataframe (pandas) για οργανωμένη ανάλυση πολλών αρχείων
* Μαζική επεξεργασία:
    * Χρήση os.listdir() για αναδρομική σάρωση φακέλων.
### Παράδειγμα επέκτασης
```bash
#Dictionary:
   {
    "data/file1.txt": "d077f...",
    "data/file2.jpg": "a3c8e...",
    "docs/report.pdf": "1b2f3..."
} 
-------
#Pandas
    hashes = {
        "file1.txt": "d077f...", 
        "file2.jpg": "a3c8e..."
    }
    df = pd.DataFrame(list(hashes.items()), columns=["File", "Hash"])
#Output
       File      Hash
0  file1.txt  d077f...
1  file2.jpg  a3c8e...
-------
#Μαζική Επεξεργασία με os.listdir()

def batch_hash_calculation(directory, algorithm='sha256'):
    results = {}
    try:
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            if os.path.isfile(full_path): 
                results[entry] = calculate_file_hash(full_path, algorithm)
    except Exception as e:
        print(f"{e}")
    return results

# Παράδειγμα χρήσης
hashes = batch_hash_calculation("my_files")
```

# 4. Ανίχνευση Αλλαγών
Ερώτημα: Παρακολούθηση αλλαγών με την πάροδο του χρόνου;

Απάντηση:
* Προσέγγιση υλοποιησης παρακουλούθησης:
    1. Περιοδικός έλεγχος μέσω cron & Task Scheduler
    2. Αποθήκευση Ιστορικού μεσω log αρχείου με timestamps
* Ειδοποιήσεις:
    * Μέσω email
    * Webhooks για real-time alerts.

## 📝 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this software under the terms of the license.
