read_cache <- function(cached_glossary_path) {
  cached_glossary <- readRDS(cached_glossary_path)
  validate_cached_glossary(cached_glossary)
  cached_glossary
}

write_cache <- function(glossary_path, entries, cached_glossary_path) {
  parsed_yaml <- yaml::read_yaml(glossary_path)

  to_cache <- list(
    uri = glossary_path,
    entries = parsed_yaml
  )

  saveRDS(to_cache, cached_glossary_path)
  to_cache
}


use_cache <- function(glossary_path, cache_path) {
  hash_glossary_path <- digest::digest(tolower(glossary_path))

  validate_glossary_cache_path(cache_path)

  cached_glossary_file_name <- paste0(
    "glossary-", hash_glossary_path, ".rds"
  )
  cached_glossary_path <- file.path(cache_path, cached_glossary_file_name)

  if (file.exists(cached_glossary_path)) {
    raw_glossary <- read_cache(cached_glossary_path)
  } else {
    raw_glossary <- write_cache(
      glossary_path,
      entries,
      cached_glossary_path
    )
  }

  raw_glossary
}
