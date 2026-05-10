# Update code in app.py
## _get_response
### Before chatRequest call apply BM25 searchig approach from previos project (class TextProcessorBM25)
#### applying BM25 should be in separate module
try to write flexible code
## add function _bootstrap() returning reference to object of TextProcessorBM25
### create object of TextProcessorBM25 with appropriate constructoring implying existence travel_agency_policy.joblib ready for use
# Update class TextProcessorBM25
## Consider BM25 search trusted if score greater than a threshold being set at constructing time (so update constructor)
investigate some reasonaable threshold by playing model and logging 10 first scores (They should be sorted). Most likely it is 1 (not 0)<br>
# Introduce separate script
In separate script save the BM25 model in travel_agency_policy.joblib
