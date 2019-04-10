using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Hangman.Models;
using Microsoft.EntityFrameworkCore;

namespace Hangman.Persistance
{
    public class HangmanContext : DbContext
    {
        public HangmanContext(DbContextOptions<HangmanContext> options) : base(options)
        {

        }

        public DbSet<Game> Games { get; set; }
        public DbSet<GuessedLetter> GuessedLetters { get; set; }
        public DbSet<Language> Languages { get; set; }
        public DbSet<LetterInfo> LetterInfos { get; set; }
        public DbSet<User> Users { get; set; }
        public DbSet<WordApproval> WordApprovals { get; set; }
        public DbSet<WordInfo> WordInfos { get; set; }
        public DbSet<WordInGame> WordsInGame { get; set; }

        protected override void OnModelCreating(ModelBuilder builder)
        {
            base.OnModelCreating(builder);
        }
    }
}
