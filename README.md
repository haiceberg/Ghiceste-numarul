# Ghicește Numărul - Prezentare generală

  Acest joc este o aplicație simplă în care utilizatorul trebuie să ghicească un număr ales aleatoriu de calculator. 
  
  Acesta dispune de un număr limitat de încercări pentru a ghici corect numărul gândit de sistem.

## Descrierea jocului

Jocul presupune ca utilizatorul să ghicească un număr între 0 și 50, iar calculatorul va oferi indicii despre numărul introdus de participant în cazul în care acesta este prea mare sau prea mic. 

Dacă jucătorul ghicește numărul corect în limita celor 5 încercări, va câștiga. 

Dacă nu reușește să ghicească numărul, acesta pierde și se va afișa numărul care trebuia ghicit.

## Funcționalități

* 1  **Numărul aleatoriu generat**
  
Calculatorul generează un număr aleatoriu între 0 și 50. Acest număr este secret și utilizatorul trebuie să-l ghicească.

* 2 **Sistemul de încercări**

Utilizatorul are 5 șanse pentru a ghici numărul corect. Dacă acesta depășește limita de încercări, jocul va afișa un mesaj de final de joc.

* 3 **Mesaje interactive**

Pe parcursul jocului, utilizatorului i se va indica dacă numărul introdus este mai mare sau mai mic decât cel gândit de calculator, oferind astfel indicii pentru a-l ajuta să ghicească.

## Detalii tehnice

### **Variabilele utilizate**:

- `numar_ghicit` - Este numărul aleatoriu generat de calculator, pe care utilizatorul trebuie să-l ghicească.
- `sanse` - Numărul de încercări pe care utilizatorul le are pentru a ghici numărul corect (5 încercări).
- `numaratoare` - O variabilă care numără câte încercări a făcut utilizatorul până în acel moment.
- `nr_meu` - Este numărul pe care jucătorul îl introduce în momentul începerii jocului.

### **Fluxul jocului**:
1. Programul afișează un mesaj introductiv, explicând regulile jocului.
2. Se generează un număr aleatoriu între 0 și 50.
3. Utilizatorul are 5 încercări pentru a ghici numărul corect.
4. După fiecare încercare, utilizatorul primește un mesaj care îi spune dacă numărul introdus este prea mare sau prea mic.
5. Dacă jucătorul ghicește numărul, jocul se încheie și i se afișează un mesaj de felicitare.
6. Dacă utilizatorul nu ghicește numărul după 5 încercări, jocul se încheie și i se afișează numărul corect.
