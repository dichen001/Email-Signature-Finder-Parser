# Email-Signature-Finder-Parser
This repo is going to work on the identification, extraction and parsing of the Signature part form Emails

##Folder Extractor contains all the main functions for processing Emails.
You can tell their functions by their name.


## Data Organization:
Find all the processed data [here](https://github.com/dichen001/talon/tree/master/tests/fixtures/signature/emails/total)
Find emails body [here](https://github.com/dichen001/talon/tree/master/tests/fixtures/signature/emails/body)
The extracted Signature Block are saved in `data/extracted_SIG` with delimeter `  @@@##@@@ ` spliting the Sig and the filename.


## Marker
```
#sig#

#name#
#title#
#comp#
#num#
#email#
#url#
```

### Examples:
`allen-p_inbox13_body`
```
If you are unavailable this week, please ensure you delegate this work out.

#sig#Happy New Year
#sig#
#sig##name#Louise
```
`allen-p_inbox22_body`
```
Phillip, there are a number of alternative systems that will allow the same
level of energy efficiency. I would wait a bit for Wink's bid though. You
say that your panel costs are $20,000 additional. that sounds like a lot. I
just did a panel house with a 2100 sq ft footprint and the total panel cost
was about $25,000 with 8 inch walls and 10 inch roof. Stay in touch and we
can discuss alternatives if that becomes necessary. If your budget is $85-90
per sq. ft.  excluding land costs your costs will be on the low end of the
true custom home level but should be achievable with good management.
#sig##name#Richard Morgan
#sig##title#Manager, Green Building Program
#sig##comp#Austin Energy
#sig##addr#721 Barton Springs Rd.
#sig##addr#Austin, TX 78704-1194
#sig##num#Ph. 512.505.3709
#sig##num#Fax 512.505.3711
#sig##email#e-mail richard.morgan@austinenergy.com
```

