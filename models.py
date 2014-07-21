# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class BlastHit(models.Model):
    hit_id = models.IntegerField(unique=True)
    query_locus = models.ForeignKey('BlastQuery', db_column='query_locus')
    subject_locus = models.ForeignKey('OrfEntry', db_column='subject_locus')
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
        managed = False
        db_table = 'blast_hit'

class BlastQuery(models.Model):
    blast_query_locus = models.ForeignKey('OrfEntry', db_column='blast_query_locus', primary_key=True)
    accession_no = models.ForeignKey('SequenceInfo', db_column='accession_no')
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
        managed = False
        db_table = 'blast_query'

class GeneBlockInfo(models.Model):
    gene_block_name = models.CharField(primary_key=True, max_length=100)
    category = models.CharField(max_length=45, blank=True)
    function = models.CharField(max_length=45, blank=True)
    notes = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'gene_block_info'

class GeneBlockMembership(models.Model):
    gene = models.CharField(primary_key=True, max_length=10)
    gene_block_name = models.ForeignKey(GeneBlockInfo, db_column='gene_block_name', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'gene_block_membership'

class Hgt(models.Model):
    hgt_id = models.IntegerField(primary_key=True)
    accession_no = models.CharField(max_length=45)
    method = models.CharField(max_length=45, blank=True)
    start = models.IntegerField(blank=True, null=True)
    stop = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hgt'

class Jobs(models.Model):
    job_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('Users', blank=True, null=True)
    job_status = models.CharField(max_length=45, blank=True)
    active = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'jobs'

class OrfEntry(models.Model):
    locus = models.CharField(primary_key=True, max_length=45)
    accession_no = models.ForeignKey('SequenceInfo', db_column='accession_no')
    start = models.IntegerField()
    stop = models.IntegerField()
    strand = models.IntegerField()
    genbank_annotation = models.ForeignKey(GeneBlockMembership, db_column='genbank_annotation', blank=True, null=True)
    product_type = models.CharField(max_length=45, blank=True)
    translation_table = models.CharField(max_length=45, blank=True)
    dna_sequence = models.TextField(blank=True)
    amino_acid_sequence = models.TextField(blank=True)
    protein_id = models.CharField(max_length=45, blank=True)
    class Meta:
        managed = False
        db_table = 'orf_entry'

class SequenceInfo(models.Model):
    accession_no = models.CharField(primary_key=True, max_length=45)
    internal_tax = models.ForeignKey('Taxonomy')
    sequence_type = models.CharField(max_length=45, blank=True)
    version = models.CharField(max_length=45, blank=True)
    date_updated = models.DateField(blank=True, null=True)
    sequence = models.TextField(blank=True)
    common_name = models.CharField(max_length=200, blank=True)
    class Meta:
        managed = False
        db_table = 'sequence_info'

class Taxonomy(models.Model):
    tax_id = models.IntegerField(primary_key=True)
    kingdom = models.CharField(max_length=45, blank=True)
    phylum = models.CharField(max_length=45, blank=True)
    class_field = models.CharField(db_column='class', max_length=45, blank=True) # Field renamed because it was a Python reserved word.
    order = models.CharField(max_length=45, blank=True)
    family = models.CharField(max_length=45, blank=True)
    genus = models.CharField(max_length=45, blank=True)
    species = models.CharField(max_length=45, blank=True)
    class Meta:
        managed = False
        db_table = 'taxonomy'

class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=45, blank=True)
    pwd = models.CharField(max_length=16, blank=True)
    email = models.CharField(max_length=62, blank=True)
    permission_level = models.CharField(max_length=45, blank=True)
    class Meta:
        managed = False
        db_table = 'users'

