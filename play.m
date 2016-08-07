# returns St with event id and timestamp.
#sequence2;
load("data.mat")
t=[1:size(data)(1)]';
[x,y] = find(data);
S(x)=y;

St=[S t];

graphics_toolkit gnuplot
figure('visible','off');
colormap('hot');

tone_step = 1.0095;

# The first time index: 0
# The last time index: size(data)(1) + 1
# Scaling to minutes:
minutes = 5;
sample_s = 0.4;
last_time_index = size(data)(1)
sound = zeros(44100*(minutes*60 + sample_s),1);
timestep = (minutes*60)/last_time_index;

for ind = 1:length(St)
  note = St(ind,1);
  time = St(ind,2);
  sample_len = floor(44100*sample_s);
  tone = sin((1:sample_len)./44100 .* 2 .* pi .* (440*(tone_step^note))) .* \
    (1 - (1/sample_len) .* (1:sample_len));
  place = floor((timestep*time * 44100)) + 1;
  sound_sample = sound(place:(place+sample_len-1));
  mixed_sound = (sound_sample + tone');
  sound(place:(place+sample_len - 1)) = mixed_sound;
endfor
sound = sound./max(abs(sound));
wavwrite(sound, 44100, 'sequence.wav');

grid = zeros(6);
nextEvent = 1;
# One video frame for each 1/10 s.
for t = [0:4410:length(sound)]
  grid = grid .* 0.9;
  note = St(ind,1);
  time = St(ind,2);
  # While the next event timestamp is smaller than equal to this time.
  while St(nextEvent,2)*timestep <= t/44100
    event = St(nextEvent,1);
    y = mod(event, 6) + 1;
    x = floor(event / 6) + 1;
    grid(x,y) = 1.0;
    nextEvent++;
  endwhile
  imagesc(grid, [0 1]);
  filename=sprintf('output/%05d.png',floor(t/4410));
  print(filename, '-dpng');
endfor

# soundsc(sound, 44100);
