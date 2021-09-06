# Distributed Systems

## Clocks

1. :fontawesome-solid-graduation-cap: [Time, Clocks, and  the Ordering of Events in a  Distributed System][1]
   :fontawesome-solid-file-pdf: : Leslie Lamport's 1978 paper on ordering of events in a distributed system.
2. [Distributed Systems: Physical, Logical, and Vector Clocks][2]: Nice post by Joe Honour explaining logical and vector
   clocks

[1]: https://lamport.azurewebsites.net/pubs/time-clocks.pdf
[2]: https://levelup.gitconnected.com/distributed-systems-physical-logical-and-vector-clocks-7ca989f5f780

## CAP Theorem

3. :fontawesome-solid-graduation-cap: [Towards Robust Distributed Systems][3] :fontawesome-solid-file-pdf: : Eric Brewer's original paper on CAP theorem.
4. :fontawesome-solid-graduation-cap: [Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services][4] :fontawesome-solid-file-pdf: : Gilbert and Lynch's proof of the CAP theorem
5. [DBMS Musings: Problems with CAP, and Yahoo’s little known NoSQL system][5]: Daniel Abadi's post about how to use PASELC instead of CAP to understand the tradeoffs in design. A paper/article on this is available [here as well][5.1] :fontawesome-solid-file-pdf:.
6. [Please stop calling databases CP or AP][6]: Martin Kleppmann's post critiquing the CAP theorem. This post has a good section on explaining linearizable consistency.
7. [CAP Theorem: You don’t need CP, you don’t want AP, and you can’t have CA][7] :fontawesome-brands-youtube: : A really good talk by Siddhartha Reddy introducing CAP and PASELC

[3]: http://www.cs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf
[4]: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.20.1495&rep=rep1&type=pdf
[5]: http://dbmsmusings.blogspot.com/2010/04/problems-with-cap-and-yahoos-little.html
[5.1]: https://www.cs.umd.edu/~abadi/papers/abadi-pacelc.pdf
[6]: https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html
[7]: https://www.youtube.com/watch?v=hUd_9FENShA

## Consistency models

8. [Strong consistency models][8]: Excellent post by Kyle Kingsbury about various consistency models.
9. :fontawesome-solid-graduation-cap: [Linearizability: A Correctness Condition for Concurrent Objects][9] :fontawesome-solid-file-pdf: : Paper on Linearizable consistency
10. :fontawesome-solid-graduation-cap: [Consistency in Non-Transactional Distributed Storage Systems][10] :fontawesome-solid-file-pdf: : A paper covering all kinds of consistency models

[8]: https://aphyr.com/posts/313-strong-consistency-models
[9]: https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf
[10]: https://arxiv.org/pdf/1512.00168.pdf

Icons used:

- :fontawesome-solid-graduation-cap: : Paper
- :fontawesome-brands-youtube:: Youtube video
- :fontawesome-solid-file-pdf:: PDF file
