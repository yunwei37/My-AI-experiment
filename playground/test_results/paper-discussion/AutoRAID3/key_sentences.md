Key Sentences from the HP AutoRAID Hierarchical Storage System Paper that Support the Main Topics and Findings:

1. **Support the Main Argument of the Paper**: 
   - "Configuring redundant disk arrays is a black art. To configure an array properly, a system administrator must understand the details of both the array and the workload it will support. Incorrect understanding of either, or changes in the workload over time, can lead to poor performance. We present a solution to this problem: a two-level storage hierarchy implemented inside a single disk-array controller." (Introduction)

2. **Support the Most Interesting, Novel Ideas or Insights**:
   - "The technology we describe in this article, known as HP AutoRAID, automatically and transparently manages migration of data blocks between these two levels as access patterns change." (Introduction)
   - "The innovation of HP AutoRAID lies in its two-level storage hierarchy managed transparently by the RAID controller." (Summary of the Features of HP AutoRAID)
   - "Adaptation to Workload Changes. As the active set of data changes, newly active data are promoted to mirrored storage, and data that have become less active are demoted to RAID 5 in order to keep the amount of mirrored data roughly constant." (Summary of the Features of HP AutoRAID)
   - "Log-Structured RAID 5 Writes. HP AutoRAID avoids this overhead in most cases by writing to its RAID 5 storage in a log-structured fashion—that is, only empty areas of disk are written to, so no old-data or old-parity reads are required." (Summary of the Features of HP AutoRAID)
   - "Finally, like most modern array controllers, HP AutoRAID takes advantage of the kind of optimization noted in Baker et al. [1991] and Ruemmler and Wilkes [1993] that become possible with nonvolatile memory." (Related Work)

3. **Support the Methodology Used**:
   - "The baseline HP AutoRAID configuration on which we report was a 12-disk system with one controller and 24MB of controller data cache." (Experimental Setup)
   - "A combination of prototyping and event-driven simulation was used in the development of HP AutoRAID." (HP AutoRAID Performance Results)

4. **Support the Results Obtained**:
   - "In Section 4 we present a set of comparative performance analyses of different algorithm and policy choices that were used to help guide the implementation of the real thing." ( HP AutoRAID Performance Results)
   - "HP AutoRAID significantly outperforms the RAID array and has performance about three-fourths that of JBOD-LVM." (Macrobenchmarks)

5. **Support the Key Findings**:
   - "The HP AutoRAID technology works extremely well, providing performance close to that of a nonredundant disk array across many workloads. At the same time, it provides full data redundancy and can tolerate failures of any single array component." (Summary)
   - "The first product based on the technology, the HP XLR1200 Advanced Disk Array, is now available." (Summary)

6. **Additional Important, Insightful, or Interesting Sentences**:
   - "If a new PEG is needed for the RAID 5 storage class, and no free PEXes are available, a mirrored PEG may be chosen for cleaning: all the data are migrated out to fill holes in other mirrored PEGs, after which the PEG can be reclaimed and reallocated to the RAID 5 storage class." (Compaction: Cleaning and Hole-Plugging)
   - "The management tool uses these statistics to suggest possible configuration choices. For example, the tool is able to determine that for a particular period of high load, performance could have been improved by adding cache memory because the array controller was short of read cache." (Management Tool)

This list represents a selection of sentences and paragraphs from the paper that align with the specified criteria and help illustrate its main topics, novel insights, methodology, results, and key findings.