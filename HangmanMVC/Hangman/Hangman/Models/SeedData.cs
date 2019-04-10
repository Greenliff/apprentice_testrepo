using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using System;
using System.Collections.Generic;
using System.Linq;
using Hangman.Persistance;

namespace Hangman.Models
{
    public static class SeedData
    {
        public static void Initialize(IServiceProvider serviceProvider)
        {
            using (var context = new HangmanContext(
                serviceProvider.GetRequiredService<
                    DbContextOptions<HangmanContext>>()))
            {
                // Look for any Words
                if (context.WordInfos.Any())
                {
                    return;   // DB has been seeded
                }

                context.WordInfos.AddRange(
                    new WordInfo
                    {
                        Word = "Test",
                        DateSubmitted = DateTime.MaxValue,
                        IsApproved = true,
                        Language = new Language
                        {
                            Games = new List<Game>(),
                            LanguageId = 0,
                            LanguageName = "Java",
                            Letters = new List<LetterInfo>(),
                            Words = new List<WordInfo>()
                        },
                        LanguageId = 0,
                        Submitter = new User
                        {
                            Games = new List<Game>(),
                            IsAdmin = true,
                            Mail = "abc@def.gh",
                            Password = "12345678",
                            UserId = 1,
                            Username = "maltamirano",
                            WordApprovals = new List<WordApproval>(),
                            Words = new List<WordInfo>()
                        },
                        SubmitterId = 1,
                        WordApprovals = new List<WordApproval>(),
                        WordId = 0,
                        WordInGames = new List<WordInGame>()
                    }
                );
                context.SaveChanges();
            }
        }
    }
}