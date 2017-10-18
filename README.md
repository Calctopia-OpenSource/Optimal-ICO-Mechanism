# An Optimal ICO Mechanism

This repository will contain an implementation of [An Optimal ICO Mechanism](https://github.com/Calctopia-OpenSource/documentation/blob/master/An%20Optimal%20ICO%20Mechanism.pdf):
* the web interface is a PHP/AJAX web application that will be open-sourced after the ICO.
* this mechanism shouldn't be fully implemented in Solidity: (1) it would consume too much gas; (2) privacy must be maintained to prevent signaling/collusion between bidders.
* a simple Solidity contract for this auction is available at [https://github.com/Calctopia-OpenSource/zeppelin-solidity/blob/master/contracts/crowdsale/AuctionSale.sol](https://github.com/Calctopia-OpenSource/zeppelin-solidity/blob/master/contracts/crowdsale/AuctionSale.sol).
* the python script [auctionVickrey-Dutch.py](https://github.com/Calctopia-OpenSource/Optimal-ICO-Mechanism/blob/master/auctionVickrey-Dutch.py) contains the implementation of the [simple clinching multi-item Vickrey-Dutch auction](http://econcs.seas.harvard.edu/files/econcs/files/mishra_geb.pdf) as used in [An Optimal ICO Mechanism](https://github.com/Calctopia-OpenSource/documentation/blob/master/An%20Optimal%20ICO%20Mechanism.pdf).


## Screenshots

Bidding page:

![Bidding](https://github.com/Calctopia-OpenSource/Optimal-ICO-Mechanism/raw/master/bidding.PNG)

Payment page:

![Payment](https://github.com/Calctopia-OpenSource/Optimal-ICO-Mechanism/raw/master/payment.PNG)
