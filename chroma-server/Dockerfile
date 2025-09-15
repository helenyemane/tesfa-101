# chroma-server/Dockerfile
FROM chromadb/chroma:0.5.3

# Expose ChromaDB HTTP port
EXPOSE 8000

# Run ChromaDB server — data stored in /chroma/chroma-data
CMD ["chroma", "run", "--host", "0.0.0.0", " --port", "8000"]