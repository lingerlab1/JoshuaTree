" FZF find and Rg
nnoremap <silent> <leader>b :Buffers<CR>
nnoremap <silent> <leader>o :Files<CR>
nnoremap <silent> <leader>s :Rg<CR>

" Ranger
nnoremap <silent> <leader>f :RnvimrToggle<CR>

" Turn off highlight
nnoremap <silent> <leader><space> :nohlsearch<CR>

" Terminal Operation
tnoremap <leader>q <c-\><c-n><cr>

" Auto format
nnoremap <F3> :Autoformat<cr>

" Spell check and quick fix
nnoremap <F4> :set spell!<cr>
nnoremap <F5> 1z=<cr>

" Ctrl-j/k deletes blank line below/above, and Alt-j/k inserts.
nnoremap <silent><C-j> m`:silent +g/\m^\s*$/d<CR>``:noh<CR>
nnoremap <silent><C-k> m`:silent -g/\m^\s*$/d<CR>``:noh<CR>
nnoremap <silent><A-j> :set paste<CR>m`o<Esc>``:set nopaste<CR>
nnoremap <silent><A-k> :set paste<CR>m`O<Esc>``:set nopaste<CR>

" Floatterm
nnoremap <silent> <leader>t :FloatermNew<CR>
let g:floaterm_keymap_toggle = '<F12>'
