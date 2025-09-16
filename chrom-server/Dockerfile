# chroma-server/Dockerfile
FROM chromadb/chroma:0.5.3

# Expose ChromaDB HTTP port
EXPOSE 8000

# Run ChromaDB server — data stored in /chroma/chroma-data
CMD ["sh", "-c", "chroma run --host 0.0.0.0 --port ${PORT:-8000}"]