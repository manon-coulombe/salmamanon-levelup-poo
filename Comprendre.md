# Comprendre

Essayez de synthétiser en binôme votre compréhension de la notion que vous avez vue (s'il s'agissait de plusieurs notions, vous pouvez répéter ce paragraphe plusieurs fois) : 

La Programmation Orientée Objet
- Quel est son rôle ? 
Rassembler un groupe de fonction et de variables au sein d'une même unité. On réfère aux variables comme des propriétés et aux fonctions comme des méthodes. 

- Quel est son intérêt ? 
C'est une méthode de programmation à l'opposée de la programmation classique dite procédurale. Elle permet d'éviter les interdépendances entre les fonctions et les variables. Le code est beaucoup plus clair grace aux 4 pilier : Encapsulation, Abstraction, Héritage, Polymorphisme.

- A-t-elle des désavantages ? 
Le code est plus lourd et complexe, parfois redondant à causes des concraintes imposées. Cette méthode demande aussi plus d'expérience. Pas forcément adaptée aux petits projets et tests de fonctionnalités.

- Y a-t-il plusieurs façons de s'en servir ? 
Cette méthode répond à des contraintes strictes qui imposent une manière assez précise de l'utiliser.

- Quelles sont les étapes importantes pour la mettre en place ? 
Création de la classe qui définit les propriétés des méthodes. Puis la création des objets qui sont des instances de la classe. 

- Quelles sont les nuances d'un langage à l'autre ? 
Il y a des languages orientés objets (comme java, php, python), ils sont donc plus adaptés à cette méthode de programmation que d'autres. Mais le principe reste toujours le même, seule la syntaxe est différente.

- Quelles sont ses alternatives ? 
La programmation fonctionnelle.


Concepts

Encapsulation : 
Consiste à cacher le fonctionnement interne de l'objet en imposant à l'utilisateur de l'objet de passer par les méthodes. Ceci permet de sécuriser les données car on limite l'accès et la modification aux variables à l'intérieur des classes. mots clés : private (pour avoir accès au private on utilise des "getter" et des "setter" pour y avoir accès) vs public. 

Abstraction : 
Mécanisme qui représente les caractéristiques essentielles sans inclure les détails de la mise en oeuvre. 

Héritage: 
Création d'une classe qui hérite de toutes les propriétés de celle dont elle est étendue, plus des nouvelles. Ce mécanisme permet d'éliminer le code redondant. 

Polymorphisme:
Le fait qu'une fonction de meme nom ne donne pas les mêmes comportements puis qu'elle est défini dans plusieurs classes. Méthode de base abstraite défini concrètement dans chacune des classes filles, ainsi à l'execution on déduit le comportement le plus adapté. 

Classe vs. Instance: 
Class = propriétés équivalent aux variables + Méthodes équivalent à des fonctions 
Instance: objet qui sont des instances de classes

Éléments de programmation

Classe: 
La classe est le schéma ou le plan qui permet de générer un objet.

this / self:
    this: refert à l'objet. 
    self: refert à la classe dans son ensemble et non à une instance spécifique. 

Constructeur:
fonction déclaré dans la classe qui indique la construction des instances de cette classe. Les fonctions de type constructeur commencent généralement par une majuscule.

Méthode: 
nom donné à une fonction dans la POO. 

Attribut: 
correspond au caractères propres à un objet. 

Propriété:
nom donné aux variables dans la classe.

Membre: 
L'ensemble des propriétés et méthodes d'un objet. 

Interface: 
Sorte de classe qui contient un ensemble de méthode publique sans logique. Une classe implémente une interface, elle doit contenir toutes les méthodes de cette interface. On peut implémenter plusieurs interfaces pour une classe. 


