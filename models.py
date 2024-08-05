# coding: utf-8
from sqlalchemy import Column, String, Integer

from database import Base

class KidneyCancer(Base):
    __tablename__ = 'kidney_cancer'

    DATE_ADDED_TO_CATALOG = Column('DATE ADDED TO CATALOG', String(255))
    PUBMEDID = Column(String(255))
    FIRST_AUTHOR = Column('FIRST AUTHOR', String(255))
    DATE = Column(String(255))
    JOURNAL = Column(String(255))
    LINK = Column(String(255))
    STUDY = Column(String(255))
    DISEASE_TRAIT = Column('DISEASE/TRAIT', String(255))
    INITIAL_SAMPLE_SIZE = Column('INITIAL SAMPLE SIZE', String(255))
    REPLICATION_SAMPLE_SIZE = Column('REPLICATION SAMPLE SIZE', String(255))
    REGION = Column(String(255))
    CHR_ID = Column(String(255))
    CHR_POS = Column(String(255))
    REPORTED_GENE_S_ = Column('REPORTED GENE(S)', String(255))
    MAPPED_GENE = Column(String(255))
    UPSTREAM_GENE_ID = Column(String(255))
    DOWNSTREAM_GENE_ID = Column(String(255))
    SNP_GENE_IDS = Column(String(255))
    UPSTREAM_GENE_DISTANCE = Column(String(255))
    DOWNSTREAM_GENE_DISTANCE = Column(String(255))
    STRONGEST_SNP_RISK_ALLELE = Column('STRONGEST SNP-RISK ALLELE', String(255))
    SNPS = Column(String(255))
    MERGED = Column(String(255))
    SNP_ID_CURRENT = Column(String(255))
    CONTEXT = Column(String(255))
    INTERGENIC = Column(String(255))
    RISK_ALLELE_FREQUENCY = Column('RISK ALLELE FREQUENCY', String(255))
    P_VALUE = Column('P-VALUE', String(255))
    PVALUE_MLOG = Column(String(255))
    P_VALUE__TEXT_ = Column('P-VALUE (TEXT)', String(255))
    OR_or_BETA = Column('OR or BETA', String(255))
    _95__CI__TEXT_ = Column('95% CI (TEXT)', String(255))
    PLATFORM__SNPS_PASSING_QC_ = Column('PLATFORM [SNPS PASSING QC]', String(255))
    CNV = Column(String(255))
    MAPPED_TRAIT = Column(String(255))
    MAPPED_TRAIT_URI = Column(String(255))
    STUDY_ACCESSION = Column('STUDY ACCESSION', String(255))
    GENOTYPING_TECHNOLOGY = Column('GENOTYPING TECHNOLOGY', String(255))
    



# class Genomics(Base):
#     __tablename__ = 'kidney cancer'

#     def __init__(self, snp=None, geneIds=None, region=None, accession=None, context=None, url=None):
#         self.snp = snp
#         self.geneIds = geneIds
#         self.region = region
#         self.accession = accession
#         self.context = context
#         self.url = url