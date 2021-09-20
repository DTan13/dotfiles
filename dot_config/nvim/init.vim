set encoding=UTF-8

set number
set ruler
set exrc
set secure

set tabstop=4
set softtabstop=4
set shiftwidth=4
set noexpandtab

if empty(glob('~/.local/share/nvim/site/autoload/plug.vim'))
  silent !curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs
        \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
endif

call plug#begin('~/.local/share/nvim/plugged')

Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'mhinz/vim-startify'
Plug 'ryanoasis/vim-devicons'

Plug 'vim-airline/vim-airline'
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#hunks#enabled = 1
let g:airline#extensions#battery#enabled = 1
let g:airline_powerline_fonts=1
let g:airline#extensions#whitespace#enabled = 0

Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'
Plug 'jiangmiao/auto-pairs'
Plug 'sbdchd/neoformat'
" Enable alignment
let g:neoformat_basic_format_align = 1

" Enable tab to space conversion
let g:neoformat_basic_format_retab = 1

" Enable trimmming of trailing whitespace
let g:neoformat_basic_format_trim = 1

" custom setting for clangformat
let g:neoformat_cpp_clangformat = {
			\ 'exe': 'clang-format',
			\ 'args': ['--style="{IndentWidth: 4}"']
			\}
let g:neoformat_enabled_cpp = ['clangformat']
let g:neoformat_enabled_c = ['clangformat']

Plug 'scrooloose/nerdtree'
Plug 'mg979/vim-visual-multi', {'branch': 'master'}

Plug 'vim-syntastic/syntastic'
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 0
let g:syntastic_check_on_wq = 0

Plug 'voldikss/vim-floaterm'

Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

Plug 'neovim/nvim-lspconfig'

" https://github.com/neovim/nvim-lspconfig/blob/master/CONFIG.md

" lsp setup for c and cpp install clang
" require'lspconfig'.clangd.setup{}

" lsp setup for shell scripts install bash-language-server
" require'lspconfig'.bashls.setup{}

" lsp setup for golang install gopls
" require'lspconfig'.gopls.setup{}

" lsp setup for python install python-lsp-server
" require'lspconfig'.pylsp.setup{}

" lsp setup for js/ts install typescript-language-server
" require'lspconfig'.tsserver.setup{}

lua << EOF
require'lspconfig'.clangd.setup{}
require'lspconfig'.bashls.setup{}
require'lspconfig'.gopls.setup{}
require'lspconfig'.pylsp.setup{}
require'lspconfig'.tsserver.setup{}
EOF

Plug 'nvim-lua/completion-nvim'
autocmd BufEnter * lua require'completion'.on_attach()

Plug 'steelsojka/completion-buffers'

let g:completion_word_min_length = 1

let g:completion_chain_complete_list = {
\ 'default': [
	\    {'complete_items': ['lsp', 'buffers' ]},
	\    {'mode': '<c-p>'},
	\    {'mode': '<c-n>'}
	\]
	\}

" Use <Tab> and <S-Tab> to navigate through popup menu
inoremap <expr> <Tab>   pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

" Set completeopt to have a better completion experience
set completeopt=menuone,noinsert,noselect

" Avoid showing message extra message when using completion
set shortmess+=c

Plug 'Yggdroot/indentLine'
let g:indentLine_setColors = 0

Plug 'preservim/nerdcommenter'
" Create default mappings
let g:NERDCreateDefaultMappings = 1
" Add spaces after comment delimiters by default
let g:NERDSpaceDelims = 1
" Use compact syntax for prettified multi-line comments
let g:NERDCompactSexyComs = 1
" Align line-wise comment delimiters flush left instead of following code indentation
let g:NERDDefaultAlign = 'left'
" Set a language to use its alternate delimiters by default
let g:NERDAltDelims_java = 1
" Add your own custom formats or override the defaults
let g:NERDCustomDelimiters = { 'c': { 'left': '/**','right': '*/' } }
" Allow commenting and inverting empty lines (useful when commenting a region)
let g:NERDCommentEmptyLines = 1
" Enable trimming of trailing whitespace when uncommenting
let g:NERDTrimTrailingWhitespace = 1
" Enable NERDCommenterToggle to check all selected lines is commented or not
let g:NERDToggleCheckAllLines = 1

call plug#end()

colorscheme dracula

" everything leader
let mapleader = ","
noremap <leader>w :w<cr>
noremap <leader>q :q<cr>
noremap <leader>tn :tabn<cr>
noremap <leader>tp :tabp<cr>
noremap <leader>tt :tabnew<cr>
noremap <leader>f :FloatermNew<cr>
noremap <leader>bd :bd<cr>
noremap <leader>% :vsp<cr>
noremap <leader>" :sp<cr>
noremap <leader>n :NERDTreeToggle<cr>
noremap <leader>p :Rg!<cr>
noremap <leader>a :so ~/.config/nvim/init.vim<cr>

" use Alt + {h,j,k,l} from anywhere
tnoremap <A-h> <C-\><C-N><C-w>h
tnoremap <A-j> <C-\><C-N><C-w>j
tnoremap <A-k> <C-\><C-N><C-w>k
tnoremap <A-l> <C-\><C-N><C-w>l
inoremap <A-h> <C-\><C-N><C-w>h
inoremap <A-j> <C-\><C-N><C-w>j
inoremap <A-k> <C-\><C-N><C-w>k
inoremap <A-l> <C-\><C-N><C-w>l
nnoremap <A-h> <C-w>h
nnoremap <A-j> <C-w>j
nnoremap <A-k> <C-w>k
nnoremap <A-l> <C-w>l
