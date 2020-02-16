---
title: Distributed Systems
date: 2017-12-08T02:06:18.000+00:00

---
<!-- TOC -->

- [Clocks](#clocks)
- [CAP Theorem](#cap-theorem)
- [Consistency models](#consistency-models)

<!-- /TOC -->

# 1. Clocks

- {{<fa4 "fa-graduation-cap">}} [Time, Clocks, and  the Ordering of Events in a  Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf) {{<fa4 "fa-file-pdf-o">}} : Leslie Lamport's 1978 paper on ordering of events in a distributed system.
- [Distributed Systems: Physical, Logical, and Vector Clocks](https://levelup.gitconnected.com/distributed-systems-physical-logical-and-vector-clocks-7ca989f5f780): Nice post by Joe Honour explaining logical and vector clocks

# 2. CAP Theorem

- {{<fa4 "fa-graduation-cap">}} [Towards Robust Distributed Systems](http://www.cs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf) {{<fa4 "fa-file-pdf-o">}} : Eric Brewer's original paper on CAP theorem.
- {{<fa4 "fa-graduation-cap">}} [Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.20.1495&rep=rep1&type=pdf) {{<fa4 "fa-file-pdf-o">}} : Gilbert and Lynch's proof of the CAP theorem
- [DBMS Musings: Problems with CAP, and Yahoo’s little known NoSQL system](http://dbmsmusings.blogspot.com/2010/04/problems-with-cap-and-yahoos-little.html): Daniel Abadi's post about how to use PASELC instead of CAP to understand the tradeoffs in design. A paper/article on this is available [here as well](https://www.cs.umd.edu/~abadi/papers/abadi-pacelc.pdf) {{<fa4 "fa-file-pdf-o">}}.
- [Please stop calling databases CP or AP](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html): Martin Kleppmann's post critiquing the CAP theorem. This post has a good section on explaining linearizable consistency.
- [CAP Theorem: You don’t need CP, you don’t want AP, and you can’t have CA](https://www.youtube.com/watch?v=hUd_9FENShA) {{<fa4 "fa-youtube">}} : A really good talk by Siddhartha Reddy introducing CAP and PASELC

# 3. Consistency models
- [Strong consistency models](https://aphyr.com/posts/313-strong-consistency-models): Excellent post by Kyle Kingsbury about various consistency models.
- {{<fa4 "fa-graduation-cap">}} [Linearizability: A Correctness Condition for Concurrent Objects](https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf) {{<fa4 "fa-file-pdf-o">}} : Paper on Linearizable consistency
- {{<fa4 "fa-graduation-cap">}} [Consistency in Non-Transactional Distributed Storage Systems](https://arxiv.org/pdf/1512.00168.pdf) {{<fa4 "fa-file-pdf-o">}} : A paper covering all kinds of consistency models

Icons used:

- {{<fa4 "fa-graduation-cap">}} : Paper
- {{<fa4 "fa-youtube">}}: Youtube video
- {{<fa4 "fa-file-pdf-o">}}: PDF file