# ---------------------------------------------------------
# Script 02 - Silver - Glue Jobs
# Tech Challenge - Fase 3 - Big Data to Analytics
# -  Objetivo: ler os 3 CSVs da camada bronze/, adicionar a coluna ano_pesquisa e gravar em Parquet na camada silver/.
# ---------------------------------------------------------

# ---------------------------------------------------------
# 1. Importar bibliotecas
# ---------------------------------------------------------

import sys
import logging

from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import lit

# ---------------------------------------------------------
# 2. Definir funções auxiliares
# ---------------------------------------------------------

# Configurar logging
def configurar_logging() -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger("silver_etl")


# Processar os dados de um ano específico
    #Le o CSV de um ano, adiciona ano_pesquisa e grava a particao em Parquet.
def processar_ano(spark, logger, ano: int, caminho_bronze: str, caminho_silver: str):
    logger.info("Processando ano %s: %s", ano, caminho_bronze)

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .option("quote", '"')
        .option("escape", '"')
        .option("multiLine", True)
        .csv(caminho_bronze)
    )
    df = df.withColumn("ano_pesquisa", lit(ano))

    total_linhas = df.count()
    logger.info("Ano %s: %s linhas lidas", ano, total_linhas)

    df.write.mode("overwrite").option("compression", "snappy").partitionBy("ano_pesquisa").parquet(caminho_silver)

    logger.info("Ano %s: gravado em %sano_pesquisa=%s/", ano, caminho_silver, ano)


# ---------------------------------------------------------
# 3. Função principal
# ---------------------------------------------------------
def main():
    logger = configurar_logging()

    # Obter argumentos do Glue Job
    args = getResolvedOptions(sys.argv, ["JOB_NAME", "BUCKET_NAME"])
    bucket = args["BUCKET_NAME"]

    # Inicializacao padrao de todo Glue Job em PySpark
    sc = SparkContext()
    glue_context = GlueContext(sc)
    spark = glue_context.spark_session
    job = Job(glue_context)
    job.init(args["JOB_NAME"], args)

    
    # Faz a interação a cada escrita
    spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")

    anos = {
        2023: f"s3://{bucket}/bronze/state_of_data/ano=2023/",
        2024: f"s3://{bucket}/bronze/state_of_data/ano=2024/",
        2025: f"s3://{bucket}/bronze/state_of_data/ano=2025/",
    }
    caminho_silver = f"s3://{bucket}/silver/state_of_data/"

    logger.info("Iniciando Bronze -> Silver para o bucket %s", bucket)

    for ano, caminho_bronze in anos.items():
        processar_ano(spark, logger, ano, caminho_bronze, caminho_silver)

    logger.info("ETL finalizado.")
    job.commit()


if __name__ == "__main__":
    main()