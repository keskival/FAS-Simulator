#!/usr/bin/octave

# Note, you need this package also, but this should be executed once only.
installed = pkg("list", "image");
if (length(installed) == 0)
    printf("Installing missing image forge package.");
    pkg install -forge image
endif

# The first parameter is the input filename without the ".mat" extension. Output will be concatenation of this and ".eps".
# The second parameter is the length of the image side.
arg_list = argv ();
input_file = arg_list{1};
side = str2num(arg_list{2});

printf("Reading file: %s\n", strcat(input_file, ".mat"))

load(input_file)
figure('visible','on');
[x,y] = find(data);
S(x)=y;
# returns S
pkg load image;
#side = ceil(sqrt(size(S)(2)))
width = side
height = ceil(length(S)/width)
S_square = reshape(postpad(S, width*height), width, height)';
imagesc(S_square);
colormap("gray")

print ("-deps", strcat(input_file, ".eps"))

#Colors = rand(36, 3);
#colormap(Colors);

