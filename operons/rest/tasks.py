from __future__ import absolute_import

from celery import shared_task, chain

@shared_task
def BlastGeneList(genes, job):
    '''
        Processes a list of genes to BLAST against the OperonEvoDB.
    '''
    pass

@shared_task
def BlastSequence(sequence, job):
    '''
        Process a sequence that has been submitted in FASTA format to BLAST against
        the OperonEvoDB.
    '''
    pass


def Workflow(in, job):
    first = BlastGeneList(in, job) if in isinstance list else BlastSequence(in, job)
    return chain(first, )
