" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
endif

call plug#begin('~/.config/nvim/autoload/plugged')

    " Intellisense
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    " FZF
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
    Plug 'junegunn/fzf.vim'
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
	Plug 'tomasr/molokai'
	Plug 'patstockwell/vim-monokai-tasty'
	Plug 'tomasiser/vim-code-dark'
	Plug 'Chiel92/vim-autoformat'
	Plug 'honza/vim-snippets'

	" Ranger
	Plug 'kevinhwang91/rnvimr'
	" Floatterm
	Plug 'voldikss/vim-floaterm'
	" Commenter
	Plug 'preservim/nerdcommenter'

call plug#end()

source $HOME/.config/nvim/coc_config.vim
let g:airline_theme='codedark'
" let g:vim_monokai_tasty_italic = 1
colorscheme codedark

" Make Ranger replace netrw
let g:rnvimr_ex_enable = 1


