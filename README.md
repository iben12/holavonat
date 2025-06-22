# Hol vannak a vonatok?

A MÁV 2025. június 21-én lekapcsolta minden elérhetőségét a régi vonatinfós térképeknek, ahol egyben látszódott az ország vasúthálózatának állapota. [Telex cikk](https://telex.hu/belfold/2025/06/21/vonatinfo-mav-megszunes-emma)

Az új EMMA rendszer nehezen használható, mintha arra lett volna kitalálva, hogy ne lehessen áttekinteni egyben az összes vonatot. Ez a weboldal az EMMA API alapján lekéri minden járat adatait és a vonatinfóhoz hasonló módon jeleníti meg.

# Holavonat weboldal forráskód és docker file-ok

Ebben a repóban megtaláljátok a szükséges fileokat a [holavonat.hu](https://holavonat.hu) lokális futtatásához. Az indításhoz egy docker-re lesz szükségetek. A klónozott repó györkérkönyvtárából futtatható a webszerver

```bash
 docker compose up 
 ```

paranccsal. A webszerver egy statikus html-t, valamint egy jsont szolgál ki a felhasználóknak. Az adatok egy cron-job segítségével frissülnek, ami percenként cseréli a ``train_data.json`` file-t a webszerverben.

A projekt egy hétvége alatt készült, tudjuk, hogy több bug is van benne, de a szűkös idő miatt ennyit sikerült összehozni.
