# coding: utf-8
from sqlalchemy import Column, FetchedValue, Integer, Text

from database import Base

class KidneyCancer(Base):
    __tablename__ = 'genomics_gwsall'

    DATE_ADDED_TO_CATALOG = Column('DATE ADDED TO CATALOG', Text)
    PUBMEDID = Column(Text)
    FIRST_AUTHOR = Column('FIRST AUTHOR', Text)
    DATE = Column(Text)
    JOURNAL = Column(Text)
    LINK = Column(Text)
    STUDY = Column(Text)
    DISEASE_TRAIT = Column('DISEASE/TRAIT', Text)
    INITIAL_SAMPLE_SIZE = Column('INITIAL SAMPLE SIZE', Text)
    REPLICATION_SAMPLE_SIZE = Column('REPLICATION SAMPLE SIZE', Text)
    REGION = Column(Text)
    CHR_ID = Column(Text)
    CHR_POS = Column(Text)
    REPORTED_GENE_S_ = Column('REPORTED GENE(S)', Text)
    MAPPED_GENE = Column(Text)
    UPSTREAM_GENE_ID = Column(Text)
    DOWNSTREAM_GENE_ID = Column(Text)
    SNP_GENE_IDS = Column(Text)
    UPSTREAM_GENE_DISTANCE = Column(Text)
    DOWNSTREAM_GENE_DISTANCE = Column(Text)
    STRONGEST_SNP_RISK_ALLELE = Column('STRONGEST SNP-RISK ALLELE', Text)
    SNPS = Column(Text)
    MERGED = Column(Text)
    SNP_ID_CURRENT = Column(Text)
    CONTEXT = Column(Text)
    INTERGENIC = Column(Text)
    RISK_ALLELE_FREQUENCY = Column('RISK ALLELE FREQUENCY', Text)
    P_VALUE = Column('P-VALUE', Text)
    PVALUE_MLOG = Column(Text)
    P_VALUE__TEXT_ = Column('P-VALUE (TEXT)', Text)
    OR_or_BETA = Column('OR or BETA', Text)
    _95__CI__TEXT_ = Column('95% CI (TEXT)', Text)
    PLATFORM__SNPS_PASSING_QC_ = Column('PLATFORM [SNPS PASSING QC]', Text)
    CNV = Column(Text)
    MAPPED_TRAIT = Column(Text)
    MAPPED_TRAIT_URI = Column(Text)
    STUDY_ACCESSION = Column('STUDY ACCESSION', Text)
    GENOTYPING_TECHNOLOGY = Column('GENOTYPING TECHNOLOGY', Text)
    id = Column(Integer, primary_key=True, server_default=FetchedValue())

    


# class Genomics(Base):
#     __tablename__ = 'kidney cancer'

#     def __init__(self, snp=None, geneIds=None, region=None, accession=None, context=None, url=None):
#         self.snp = snp
#         self.geneIds = geneIds
#         self.region = region
#         self.accession = accession
#         self.context = context
#         self.url = url