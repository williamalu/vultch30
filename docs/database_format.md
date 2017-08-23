# Data Formats in Mongo Stats Database

## Mongo Collections

* Users: Single person
* Clubs: Group of people/teams at a school
* Teams: Group of 1-5 players in a club

## Data Formats

**User in Users Collection**

```
{'_id': 'Kathryn Hite',
 'pass': 'password',
 'onboard': '2017-09-01',
 'type': 'lead',
 'status': 'active',
 'years': '2015-2018'
 'stats': {'T': 0
	   'W': 0,
	   'L': 0,
	   'GP': 0,
	   'TUH': 0,
	   'Points': 0,
	   'P': 0,
	   'TU': 0,
	   'I': 0,
	   'P%': 0,
	   'PPTUH': 0,
	   'PP20TUH': 0}} 
```	   

**Club in Clubs Collection**

```
{'_id': 'Olin College',
 'onboard': '2017-09-01',
 'players': ['Kathryn Hite',
	     'William Lu'],
 'teams': ['Olin A',
	   'Olin B']
 'stats': [ TODO ]}

```
**Team in Teams Collection**

TODO
