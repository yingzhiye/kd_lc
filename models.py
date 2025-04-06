# coding: utf-8
from sqlalchemy import Column, FetchedValue, Integer, Text, String, Double

from database import Base

class GenomicModel(Base):
    __tablename__ = 'show_genomics_gwsall'

    # DATE_ADDED_TO_CATALOG = Column('DATE ADDED TO CATALOG', Text)
    PUBMEDID = Column(Text)
    # FIRST_AUTHOR = Column('FIRST AUTHOR', Text)
    # DATE = Column(Text)
    # JOURNAL = Column(Text)
    LINK = Column(Text)
    STUDY = Column(Text)
    # DISEASE_TRAIT = Column('DISEASE/TRAIT', Text)
    # INITIAL_SAMPLE_SIZE = Column('INITIAL SAMPLE SIZE', Text)
    # REPLICATION_SAMPLE_SIZE = Column('REPLICATION SAMPLE SIZE', Text)
    # REGION = Column(Text)
    CHR_ID = Column(Text)
    CHR_POS = Column(Text)
    # REPORTED_GENE_S_ = Column('REPORTED GENE(S)', Text)
    MAPPED_GENE = Column(Text)
    # UPSTREAM_GENE_ID = Column(Text)
    # DOWNSTREAM_GENE_ID = Column(Text)
    SNP_GENE_IDS = Column(Text)
    # UPSTREAM_GENE_DISTANCE = Column(Text)
    # DOWNSTREAM_GENE_DISTANCE = Column(Text)
    # STRONGEST_SNP_RISK_ALLELE = Column('STRONGEST SNP-RISK ALLELE', Text)
    # SNPS = Column(Text)
    # MERGED = Column(Text)
    # SNP_ID_CURRENT = Column(Text)
    CONTEXT = Column(Text)
    # INTERGENIC = Column(Text)
    # RISK_ALLELE_FREQUENCY = Column('RISK ALLELE FREQUENCY', Text)
    # P_VALUE = Column('P-VALUE', Text)
    # PVALUE_MLOG = Column(Text)
    # P_VALUE__TEXT_ = Column('P-VALUE (TEXT)', Text)
    # OR_or_BETA = Column('OR or BETA', Text)
    # _95__CI__TEXT_ = Column('95% CI (TEXT)', Text)
    # PLATFORM__SNPS_PASSING_QC_ = Column('PLATFORM [SNPS PASSING QC]', Text)
    # CNV = Column(Text)
    MAPPED_TRAIT = Column(Text)
    # MAPPED_TRAIT_URI = Column(Text)
    # STUDY_ACCESSION = Column('STUDY ACCESSION', Text)
    # GENOTYPING_TECHNOLOGY = Column('GENOTYPING TECHNOLOGY', Text)
    id = Column(Integer, primary_key=True, server_default=FetchedValue())

    
class GeneTranModel(Base):
    __tablename__ = 'show_gene_tran'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    Symbol = Column(String(255))
    Description = Column(String(255))
    Category = Column(String(255))
    Score = Column(Double(53))
    Molecular = Column(String(255))
    Variation = Column(String(255))
    Experimental = Column(String(255))
    Inferred = Column(String(255))
    PMIDs = Column(String(255))



class RelatedTranModel(Base):
    __tablename__ = 'show_related_tran'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    Name = Column(String(255))
    Score = Column(Double(53))
    Related_Genes = Column('Related Genes', String(255))

class ProteinModel(Base):
    __tablename__ = 'show_protein'

    DiseaseEntry_ID = Column('DiseaseEntry ID', String(255), primary_key=True)
    Name = Column(Text)
    Keywords = Column(Text)
    Alternative_Names = Column('Alternative Names', Text)
    Statistics = Column(Text)
    Description = Column(Text)
    Mnemonic = Column(Text)
    Cross_Reference = Column('Cross Reference', Text)


'''逆向生成models.py'''
# flask-sqlacodegen "postgresql://postgres:3@10.91.221.46:5432/KidneyBioDB" --tables kidney_cancer,kidney_disease --notables --outfile models.py --flask