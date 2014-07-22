from __future__ import unicode_literals
from django.db import models

##############################################################
#                                                            #
#              Beginning of Sequence/Gene tables             #
#                                                            #
##############################################################

class Taxonomy(models.Model):
    tax_id = models.IntegerField(primary_key=True)
    kingdom = models.CharField(max_length=45, blank=True)
    phylum = models.CharField(max_length=45, blank=True)
    # Field below renamed because it was a Python reserved word.
    class_field = models.CharField(db_column='class', max_length=45, blank=True)
    order = models.CharField(max_length=45, blank=True)
    family = models.CharField(max_length=45, blank=True)
    genus = models.CharField(max_length=45, blank=True)
    species = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = 'taxonomy'
        app_label = u'operons.rest'

class SequenceInfo(models.Model):
    accession_no = models.CharField(unique=True, max_length=45)
    internal_tax = models.ForeignKey(Taxonomy)
    sequence_type = models.CharField(max_length=45, blank=True)
    version = models.CharField(max_length=45, blank=True)
    date_updated = models.DateField(blank=True, null=True)
    sequence = models.TextField(blank=True)
    common_name = models.CharField(max_length=200, blank=True)
    class Meta:
        db_table = 'sequence_info'
        app_label = u'operons.rest'


class GeneBlock(models.Model):
    gene_block_name = models.CharField(unique=True, max_length=100)
    category = models.CharField(max_length=45, blank=True)
    function = models.CharField(max_length=45, blank=True)
    notes = models.CharField(max_length=250, blank=True)
    class Meta:
        db_table = u'gene_block_info'
        app_label = u'operons.rest'

class Gene(models.Model):
    name = models.CharField(unique=True, max_length=10)
    class Meta:
        db_table = u'gene'
        app_label = u'operons.rest'

class GeneBlockMembership(models.Model):
    gene = models.ForeignKey(Gene)
    gene_block = models.ForeignKey(GeneBlockInfo)
    class Meta:
        unique_together = ('gene', 'gene_block')
        db_table = u'gene_block_membership'
        app_label = u'operons.rest'

##############################################################
#                                                            #
#              Beginning of Blast tables                     #
#                                                            #
##############################################################

class OrfEntry(models.Model):
    locus = models.CharField(unique=True, max_length=45)
    accession_no = models.ForeignKey(SequenceInfo)
    start = models.IntegerField()
    stop = models.IntegerField()
    strand = models.IntegerField()
    genbank_annotation = models.ForeignKey(Gene, blank=True, null=True)
    product_type = models.CharField(max_length=45, blank=True)
    translation_table = models.CharField(max_length=45, blank=True)
    dna_sequence = models.TextField(blank=True)
    amino_acid_sequence = models.TextField(blank=True)
    protein_id = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = 'orf_entry'
        app_label = u'operons.rest'

class BlastQuery(models.Model):
    blast_query_locus = models.ForeignKey(OrfEntry, unique=True)
    accession_no = models.ForeignKey(SequenceInfo)
    start = models.IntegerField()
    stop = models.IntegerField()
    strand = models.IntegerField()
    genbank_annotation = models.CharField(max_length=10, blank=True)
    product_type = models.CharField(max_length=45, blank=True)
    translation_table = models.CharField(max_length=45, blank=True)
    dna_sequence = models.TextField(blank=True)
    amino_acid_sequence = models.TextField(blank=True)
    protein_id = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'blast_query'
        app_label = u'operons.rest'

class BlastHit(models.Model):
    query_locus = models.ForeignKey(BlastQuery)
    subject_locus = models.ForeignKey(OrfEntry)
    aligned_length = models.IntegerField()
    bits_score = models.FloatField()
    e_val = models.FloatField()
    align_subject_stop = models.IntegerField()
    align_subject_start = models.IntegerField()
    align_query_stop = models.IntegerField()
    align_query_start = models.IntegerField()
    number_gaps = models.IntegerField()
    number_mismatched = models.IntegerField()
    percent_ident = models.FloatField()
    class Meta:
        db_table = u'blast_hit'
        app_label = u'operons.rest'

class Hgt(models.Model):
    accession_no = models.CharField(max_length=45)
    method = models.CharField(max_length=45, blank=True)
    start = models.IntegerField(blank=True, null=True)
    stop = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    class Meta:
        db_table = 'hgt'
        app_label = u'operons.rest'

##############################################################
#                                                            #
#              Beginning of Job Management tables            #
#                                                            #
##############################################################

class RequestJob(models.Model):
    status = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True, editable=False)
    lastModified = models.DateTimeField(auto_now=True)
    result = models.ForeignKey(RequestResult, null=True, unique=True, default=None)
    completed = models.FloatField()

    class Meta:
        db_table = u'requestjob'
        app_label = u'operons.rest'

class RequestResult(models.Model):
    '''
        The representation of the output of the OperonEvoDB service.
    '''
    dateCreated = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = u'requestresult'
        app_label = u'operons.rest'
