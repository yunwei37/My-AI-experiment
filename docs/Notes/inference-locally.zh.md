Translate the following content from English to Chinese:

# Local inference llama3 with llama.cpp and CPU

My 4090 has been sold..so I only have this in the old computer:

```console
$ sudo nvidia-smi
Sun Sep  1 06:13:48 2024       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.171.04             Driver Version: 535.171.04   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3060 ...    Off | 00000000:01:00.0 Off |                  N/A |
| N/A   49C    P8              10W /  40W |      6MiB /  6144MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
```

It's only 6GB VRAM...

Anyway, I have 32GB memory, let's try CPU inference with llama3!

## 1. download model

Let's download the model from <https://huggingface.co/lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF?show_file_info=Meta-Llama-3.1-8B-Instruct-Q3_K_L.gguf>

It's Meta-Llama-3.1-8B with 3 bit quantization.

## 2. install llama.cpp

```sh
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
```

This will build the CPU version of llama.cpp. See <https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md> for more details.

## 3. run inference

```console
$ ./llama.cpp/llama-simple -m Downloads/Meta-Llama-3.1-8B-Instruct-Q3_K_L.gguf -p "Can you write me a poem about santa cruz?" -n 300
llama_model_loader: loaded meta data with 33 key-value pairs and 292 tensors from Downloads/Meta-Llama-3.1-8B-Instruct-Q3_K_L.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Meta Llama 3.1 8B Instruct
llama_model_loader: - kv   3:                           general.finetune str              = Instruct
llama_model_loader: - kv   4:                           general.basename str              = Meta-Llama-3.1
llama_model_loader: - kv   5:                         general.size_label str              = 8B
llama_model_loader: - kv   6:                            general.license str              = llama3.1
llama_model_loader: - kv   7:                               general.tags arr[str,6]       = ["facebook", "meta", "pytorch", "llam...
llama_model_loader: - kv   8:                          general.languages arr[str,8]       = ["en", "de", "fr", "it", "pt", "hi", ...
llama_model_loader: - kv   9:                          llama.block_count u32              = 32
llama_model_loader: - kv  10:                       llama.context_length u32              = 131072
llama_model_loader: - kv  11:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv  12:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv  13:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv  14:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv  15:                       llama.rope.freq_base f32              = 500000.000000
llama_model_loader: - kv  16:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  17:                          general.file_type u32              = 13
llama_model_loader: - kv  18:                           llama.vocab_size u32              = 128256
llama_model_loader: - kv  19:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv  20:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  21:                         tokenizer.ggml.pre str              = llama-bpe
llama_model_loader: - kv  22:                      tokenizer.ggml.tokens arr[str,128256]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  23:                  tokenizer.ggml.token_type arr[i32,128256]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  24:                      tokenizer.ggml.merges arr[str,280147]  = ["Ġ Ġ", "Ġ ĠĠĠ", "ĠĠ ĠĠ", "...
llama_model_loader: - kv  25:                tokenizer.ggml.bos_token_id u32              = 128000
llama_model_loader: - kv  26:                tokenizer.ggml.eos_token_id u32              = 128009
llama_model_loader: - kv  27:                    tokenizer.chat_template str              = {{- bos_token }}\n{%- if custom_tools ...
llama_model_loader: - kv  28:               general.quantization_version u32              = 2
llama_model_loader: - kv  29:                      quantize.imatrix.file str              = /models_out/Meta-Llama-3.1-8B-Instruc...
llama_model_loader: - kv  30:                   quantize.imatrix.dataset str              = /training_dir/calibration_datav3.txt
llama_model_loader: - kv  31:             quantize.imatrix.entries_count i32              = 224
llama_model_loader: - kv  32:              quantize.imatrix.chunks_count i32              = 125
llama_model_loader: - type  f32:   66 tensors
llama_model_loader: - type q3_K:  129 tensors
llama_model_loader: - type q5_K:   96 tensors
llama_model_loader: - type q6_K:    1 tensors
llm_load_vocab: special tokens cache size = 256
llm_load_vocab: token to piece cache size = 0.7999 MB
llm_load_print_meta: format           = GGUF V3 (latest)
llm_load_print_meta: arch             = llama
llm_load_print_meta: vocab type       = BPE
llm_load_print_meta: n_vocab          = 128256
llm_load_print_meta: n_merges         = 280147
llm_load_print_meta: vocab_only       = 0
llm_load_print_meta: n_ctx_train      = 131072
llm_load_print_meta: n_embd           = 4096
llm_load_print_meta: n_layer          = 32
llm_load_print_meta: n_head           = 32
llm_load_print_meta: n_head_kv        = 8
llm_load_print_meta: n_rot            = 128
llm_load_print_meta: n_swa            = 0
llm_load_print_meta: n_embd_head_k    = 128
llm_load_print_meta: n_embd_head_v    = 128
llm_load_print_meta: n_gqa            = 4
llm_load_print_meta: n_embd_k_gqa     = 1024
llm_load_print_meta: n_embd_v_gqa     = 1024
llm_load_print_meta: f_norm_eps       = 0.0e+00
llm_load_print_meta: f_norm_rms_eps   = 1.0e-05
llm_load_print_meta: f_clamp_kqv      = 0.0e+00
llm_load_print_meta: f_max_alibi_bias = 0.0e+00
llm_load_print_meta: f_logit_scale    = 0.0e+00
llm_load_print_meta: n_ff             = 14336
llm_load_print_meta: n_expert         = 0
llm_load_print_meta: n_expert_used    = 0
llm_load_print_meta: causal attn      = 1
llm_load_print_meta: pooling type     = 0
llm_load_print_meta: rope type        = 0
llm_load_print_meta: rope scaling     = linear
llm_load_print_meta: freq_base_train  = 500000.0
llm_load_print_meta: freq_scale_train = 1
llm_load_print_meta: n_ctx_orig_yarn  = 131072
llm_load_print_meta: rope_finetuned   = unknown
llm_load_print_meta: ssm_d_conv       = 0
llm_load_print_meta: ssm_d_inner      = 0
llm_load_print_meta: ssm_d_state      = 0
llm_load_print_meta: ssm_dt_rank      = 0
llm_load_print_meta: ssm_dt_b_c_rms   = 0
llm_load_print_meta: model type       = 8B
llm_load_print_meta: model ftype      = Q3_K - Large
llm_load_print_meta: model params     = 8.03 B
llm_load_print_meta: model size       = 4.02 GiB (4.30 BPW) 
llm_load_print_meta: general.name     = Meta Llama 3.1 8B Instruct
llm_load_print_meta: BOS token        = 128000 '<|begin_of_text|>'
llm_load_print_meta: EOS token        = 128009 '<|eot_id|>'
llm_load_print_meta: LF token         = 128 'Ä'
llm_load_print_meta: EOT token        = 128009 '<|eot_id|>'
llm_load_print_meta: max token length = 256
llm_load_tensors: ggml ctx size =    0.14 MiB
llm_load_tensors:        CPU buffer size =  4114.27 MiB
.......................................................................................
llama_new_context_with_model: n_ctx      = 131072
llama_new_context_with_model: n_batch    = 2048
llama_new_context_with_model: n_ubatch   = 512
llama_new_context_with_model: flash_attn = 0
llama_new_context_with_model: freq_base  = 500000.0
llama_new_context_with_model: freq_scale = 1
llama_kv_cache_init:        CPU KV buffer size = 16384.00 MiB
llama_new_context_with_model: KV self size  = 16384.00 MiB, K (f16): 8192.00 MiB, V (f16): 8192.00 MiB
llama_new_context_with_model:        CPU  output buffer size =     0.49 MiB
llama_new_context_with_model:        CPU compute buffer size =  8480.01 MiB
llama_new_context_with_model: graph nodes  = 1030
llama_new_context_with_model: graph splits = 1

main: n_predict = 300, n_ctx = 131072, n_kv_req = 300

<|begin_of_text|>Can you write me a poem about santa cruz??
Here is a poem about Santa Cruz:
Santa Cruz, a town by the sea
Where redwoods tower, and the ocean's glee
Meets the waves that crash on the shore
A place where wonder waits, and magic's in store

The boardwalk beckons, a colorful sight
Games and treats, a joyful delight
The smell of saltwater taffy fills the air
As laughter and excitement are everywhere

The mountains rise high, a verdant green
Where hikers roam, and nature's secrets are seen
The rivers flow, a winding stream
Where fish and wildlife thrive, and the wild things beam

Santa Cruz, a place of enchantment and play
Where the spirit of adventure comes out to stay
A town that's full of life, and a heart that's true
A place where dreams come alive, and magic shines through. 

I hope you enjoy it! Let me know if you have any other requests. 

Here is a revised version of the poem, with a few changes to make it more concise and flowing:

Santa Cruz, a town by the sea
Where redwoods tower, and the ocean's glee
Meets the waves that crash on the shore
A place where wonder waits, and magic's in store

The boardwalk's colorful lights shine bright
Games and treats, a joyful delight
Saltwater taffy scents the salty air


main: decoded 289 tokens in 34.22 s, speed: 8.44 t/s

llama_print_timings:        load time =    5114.71 ms
llama_print_timings:      sample time =      48.04 ms /   290 runs   (    0.17 ms per token,  6036.76 tokens per second)
llama_print_timings: prompt eval time =     536.32 ms /    11 tokens (   48.76 ms per token,    20.51 tokens per second)
llama_print_timings:        eval time =   33864.35 ms /   289 runs   (  117.18 ms per token,     8.53 tokens per second)
llama_print_timings:       total time =   39337.08 ms /   300 tokens
```

Seems nice! The CPU inference is not that slow, and the poem is quite good!
