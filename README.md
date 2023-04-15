# Shielded Execution Trace for Sangria Prover

This repository contains an notes and computations for modification of Sangia protocol, providing shielded delegated proving with zk property.
It demonstrates how to build a high entropy execution trace that can be merged with an accumulator and shown by an untrusted prover without data leaks. This approach enables O(N) execution on thin clients and offloads O(N log N) computations to a server, while preserving privacy.

## Contents

- [`shielded-sangria.md`](https://github.com/snjax/sangria-delegated-zk/blob/master/shielded-sangria.md): A detailed explanation of the shielded execution trace for Sangria prover, covering its implementation and zero-knowledge properties. Cross-posted on [zkresearch](https://zkresear.ch/t/running-sangria-final-proof-in-shielded-mode-on-untrusted-3rd-party-prover/133).
- `src/main.py`: Some symbolic computations for the notes

## Dependencies

- SageMath: The script relies on SageMath for symbolic computations. Install SageMath from [here](https://www.sagemath.org/download.html).

